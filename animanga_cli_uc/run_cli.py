#imports
from . import jikan_calls
from . import text_processing
import os
from datetime import datetime

#Text colour class
class TextColour:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

def anime_entry_texts(data: list, detail: bool = False, single: bool = False):
    titles = []
    airingStatus = []
    scores = []
    showType = []
    episodeCount = []
    synopsis = []
    broadcast = []
    # try:
    if single:
        item = data['data']

        titles.append(item['titles'][0]['title'])
        airingStatus.append(item['airing'])
        scores.append(item['score'])
        showType.append(item['type'])
        episodeCount.append(item['episodes'])
        synopsis.append(item['synopsis'])
        broadcast.append(item['broadcast']['string'])
    else:
        for result in data:
            for item in result['data']:
                titles.append(item['titles'][0]['title'])
                airingStatus.append(item['airing'])
                scores.append(item['score'])
                showType.append(item['type'])
                episodeCount.append(item['episodes'])
                synopsis.append(item['synopsis'])
                broadcast.append(item['broadcast']['string'])
    # except:
    #     # print(data)
    #     data = data['data']
    #     titles.append(data['title'])
    #     airingStatus.append(data['airing'])
    #     scores.append(data['score'])
    #     showType.append(data['type'])
    #     episodeCount.append(data['episodes'])
    #     synopsis.append(data['synopsis'])

    entry_texts = []
    for pos,title in enumerate(titles):
        entry_text = ''
        #numberTXT =  " (" + str(pos+1) + ") > "
        entry_text += TextColour.BOLD + title.strip() + TextColour.END + ' '
        if episodeCount[pos] and episodeCount[pos] > 1:
            entry_text += TextColour.BLUE + '[' + str(episodeCount[pos]) + ']' + TextColour.END + ' '
        # elif episodeCount[pos] == 1:
        #     pass
        # else:
        #    entry_text += TextColour.BLUE + ' [?]' + TextColour.END
        if showType[pos]:
            entry_text += TextColour.CYAN + showType[pos] + TextColour.END + ' '
        if airingStatus[pos]:
            entry_text += TextColour.GREEN + 'Airing' + TextColour.END + ' '
        if scores[pos]:
            entry_text += TextColour.YELLOW + 'Score: ' + str(scores[pos]) + TextColour.END + ' '
        if broadcast[pos] and airingStatus[pos]:
            entry_text += TextColour.RED + broadcast[pos] + TextColour.END + ' '

        if detail and synopsis[pos]:
            synopsisTitle = "|-> " + TextColour.UNDERLINE + "Synopsis:" + TextColour.END
            synopsisTitle = text_processing.left_margin(synopsisTitle, margin=7)[0]
            synopsisTXT = " ".join(synopsis[pos].rstrip().split())
            processed_synopsisTXT = text_processing.left_margin(synopsisTXT, margin=9)

            entry_text += "\n" + synopsisTitle
            for line in processed_synopsisTXT:
                entry_text += "\n" + line

        entry_texts.append(entry_text)

    return entry_texts

def anime_entry_text(data: dict):
    entry_text = ''
    title = data['title']
    airingStatus = data['airing']
    score = data['score']
    showType = data['type']
    episodeCount = data['episodes']
    synopsis = data['synopsis']

    entry_text += TextColour.BOLD + title.strip() + TextColour.END + ' '
    if episodeCount and episodeCount > 1:
        entry_text += TextColour.BLUE + '[' + str(episodeCount) + ']' + TextColour.END + ' '
    # elif episodeCount == 1:
    #     pass
    # else:
    #    entry_text += TextColour.BLUE + ' [?]' + TextColour.END
    if showType:
        entry_text += TextColour.CYAN + showType + TextColour.END + ' '
    if airingStatus:
        entry_text += TextColour.GREEN + 'Airing' + TextColour.END + ' '
    if score:
        entry_text += TextColour.YELLOW + 'Score: ' + str(score) + TextColour.END + ' '

    if synopsis:
        synopsisTitle = "|-> " + TextColour.UNDERLINE + "Synopsis:" + TextColour.END
        synopsisTitle = text_processing.left_margin(synopsisTitle, margin=7)[0]
        synopsisTXT = " ".join(synopsis.rstrip().split())
        processed_synopsisTXT = text_processing.left_margin(synopsisTXT, margin=9)

        entry_text += "\n" + synopsisTitle
        for line in processed_synopsisTXT:
            entry_text += "\n" + line

    return entry_text

def print_anime_info(data: dict):
    entry_texts = anime_entry_texts(data) #TEMP wrap in list to use same function

    justifyN = len(str(len(entry_texts))) + 6
    for pos,text in enumerate(entry_texts):
        numberTXT = " (" + str(pos+1) + ") > "
        print(TextColour.PURPLE + numberTXT.rjust(justifyN) + TextColour.END + text)

def print_anime_info_detail(data: dict, amount: int = 0, single: bool = False):
    entry_texts = anime_entry_texts(data, detail=True, single=single)

    justifyN = len(str(amount)) + 6
    for pos,text in enumerate(entry_texts):
        if amount!= 0 and pos >= amount:
            break
        numberTXT = " (" + str(pos+1) + ") > "
        print(TextColour.PURPLE + numberTXT.rjust(justifyN) + TextColour.END + text)

def anime(args):
    if args.which == 'anime/search':
        if args.amount <= 0:
            print(TextColour.RED + 'Amount has to be hihger than 0.' + TextColour.END)
            exit(1)

        query = args.query
        results = jikan_calls.search(callpath='anime', query=query)
        print_anime_info_detail(results, args.amount)
        
    elif args.which == 'anime/seasonal':
        # if args.current and (args.year or args.season):
        #     raise ValueError('Cannot specify year or season when using --current.')

        if args.year and args.season:
            year = args.year
            season = args.season
            results = jikan_calls.seasonal(callpath='anime',
                                            year=year,
                                            season=season)
        elif not args.year and not args.season:
            results = jikan_calls.seasonal(callpath='anime')
        
        print_anime_info(results)

    elif args.which == 'anime/random':
        results = jikan_calls.random(type='anime')
        print_anime_info_detail(results, single=True)

    elif args.which == 'anime/schedule':
        if args.day == 'today':
            day = datetime.today().strftime('%A').lower() #get current day
            print(day)
            results = jikan_calls.schedule(day=day)
            print_anime_info(results)
        else:
            day = args.day
            results = jikan_calls.schedule(day=day)
            print_anime_info(results)

    elif args.which == 'anime/top':
        # if args.type == 'upcoming':
        #     results = jikan_calls.top(type='anime', filter='upcoming')
        #     print_anime_info(results)
        # elif args.type == 'tv':
        #     results = jikan_calls.top(type='anime', filter='tv')
        #     print_anime_info(results)
        # elif args.type == 'movie':
        #     results = jikan_calls.top(type='anime', filter='movie')
        #     print_anime_info(results)
        # elif args.type == 'ova':
        #     results = jikan_calls.top(type='anime', filter='ova')
        #     print_anime_info(results)
        
        results = jikan_calls.top(type='anime', filter=args.type)
        print_anime_info(results)

def main(args):
    if args.which.startswith('anime'):
        anime(args)
    else:
        pass