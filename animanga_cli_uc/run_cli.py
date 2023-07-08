#imports
from . import jikan_calls
from . import text_processing
import os

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

def anime_entry_text(data: dict, detail: bool = False):
    titles = []
    airingStatus = []
    scores = []
    showType = []
    episodeCount = []
    synopsis = []
    for result in data:
        for item in result['data']:
            titles.append(item['titles'][0]['title'])
            airingStatus.append(item['airing'])
            scores.append(item['score'])
            showType.append(item['type'])
            episodeCount.append(item['episodes'])
            synopsis.append(item['synopsis'])

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

        if detail:
            synopsisTXT = "- Synopsis: " + " ".join(synopsis[pos].rstrip().split())
            processed_synopsisTXT = text_processing.left_margin(synopsisTXT, margin=10)
            for line in processed_synopsisTXT:
                entry_text += "\n" + line

        entry_texts.append(entry_text)

    return entry_texts

def print_anime_info(data: dict):
    entry_texts = anime_entry_text(data)

    justifyN = len(str(len(entry_texts))) + 6
    for pos,text in enumerate(entry_texts):
        print(TextColour.PURPLE + " (" + str(pos+1) + ") > " + TextColour.END + text)

def print_anime_info_detail(data: dict):
    entry_texts = anime_entry_text(data, detail=True)

    justifyN = len(str(len(entry_texts))) + 6
    for pos,text in enumerate(entry_texts):
        if pos >= 3:
            break
        print(TextColour.PURPLE + " (" + str(pos+1) + ") > " + TextColour.END + text)

def anime(args):
    if args.which == 'anime/search':
        query = args.query
        results = jikan_calls.search(callpath='anime', query=query)
        print_anime_info_detail(results)
        
    elif args.which == 'anime/seasonal':
        if args.current and (args.year or args.season):
            raise ValueError('Cannot specify year or season when using --current.')

        if args.current:
            results = jikan_calls.seasonal(callpath='anime')
        else:
            year = args.year
            season = args.season
            results = jikan_calls.seasonal(callpath='anime',
                                            year=year,
                                            season=season)
        
        print_anime_info(results)

def main(args):
    if args.which.startswith('anime'):
        anime(args)
    else:
        pass