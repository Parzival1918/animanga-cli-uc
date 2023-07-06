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

def get_input(question: str = "Search query: "):
    print(TextColour.BOLD + TextColour.YELLOW + question + TextColour.END, end='')
    return input()

def main(args):
    userInput = get_input()
    results = jikan_calls.searchAnime(userInput)
    print(results)