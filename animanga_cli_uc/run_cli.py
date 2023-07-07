#imports
from . import jikan_calls

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

def print_info(data: dict):
    titles = []
    airingStatus = []
    scores = []
    showType = []
    for result in data:
        for item in result['data']:
            titles.append(item['titles'][0]['title'])
            airingStatus.append(item['airing'])
            scores.append(item['score'])
            showType.append(item['type'])

    justifyN = len(str(len(titles))) + 6
    for pos,title in enumerate(titles):
        numberTXT =  " (" + str(pos+1) + ") > "
        print(TextColour.PURPLE + numberTXT.rjust(justifyN) + TextColour.END, end='')
        print(TextColour.BOLD + title + TextColour.END, end=' ')
        if showType[pos]:
            print(TextColour.CYAN + showType[pos] + TextColour.END, end=' ')
        if airingStatus[pos]:
            print(TextColour.GREEN + 'Airing' + TextColour.END, end=' ')
        if scores[pos]:
            print(TextColour.YELLOW + 'Score: ' + str(scores[pos]) + TextColour.END, end=' ')

        print() #newline

def anime(args):
    if args.which == 'anime/search':
        query = args.search
        results = jikan_calls.search(callpath='anime', query=query)
        print(results)
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
        
        print_info(results)

def main(args):
    if args.which.startswith('anime'):
        anime(args)
    else:
        pass