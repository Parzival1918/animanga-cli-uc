import curses
from . import jikan_calls

def redrawMenu(stdscr, menuContents, selectedMenu):
    #Print menu
    menu_y = 0
    menu_x = 1
    stdscr.move(menu_y, menu_x) #move cursor to top left
    for pos, menuItem in enumerate(menuContents):
        if pos == selectedMenu:
            stdscr.addstr(menuItem, curses.A_UNDERLINE)
        else:
            stdscr.addstr(menuItem)
        menu_x += len(menuItem) + 3
        stdscr.move(menu_y, menu_x) #move cursor

def redrawContent(window, manuSelected):
    window.clear()

    window.border() #draw border

    #Print content
    if manuSelected == 'Manga':
        window.addstr(1, 1, 'Manga')
    elif manuSelected == 'Anime':
        window.addstr(1, 1, 'Anime')
    else:
        window.addstr(1, 1, 'Unknown')

    #Add personal info at bottom left
    window.addstr(window.getmaxyx()[0]-1, 1, 'by @UnstrayCato')

    window.refresh()

def ui_main(stdscr):
    #imports

    #Create pair of colors
    # curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    # SELECTED_MENU_ITEM = curses.color_pair(1)

    #Set cursor to invisible
    curses.curs_set(0)

    #Don't wait for input when calling getch
    stdscr.nodelay(True)

    #Menu options
    menuContents = ['Manga', 'Anime']
    selectedMenu = 0

    #Get screen dimensions
    height, width = stdscr.getmaxyx()
    #Content window
    contentWindow = curses.newwin(height-1, width, 1, 0)

    #Print to screen first time
    stdscr.clear()

    redrawMenu(stdscr, menuContents, selectedMenu)

    stdscr.refresh()

    redrawContent(contentWindow, menuContents[selectedMenu])

    #Run in while leep True until user presses 'q'
    while True:
        try:
            #Get user input
            key = stdscr.getch()
        except:
            #No input
            key = None

        if key == ord('q'):
            break
        else:
            #Update contents depending on user input
            if key == ord('n'):
                #Move cursor right
                selectedMenu += 1
                if selectedMenu >= len(menuContents):
                    selectedMenu = 0
                
                #Print menu
                stdscr.clear()
                redrawMenu(stdscr, menuContents, selectedMenu)
                stdscr.refresh()

                redrawContent(contentWindow, menuContents[selectedMenu])
            
        pass

def main():
    #imports
    from curses import wrapper

    #wrapper
    wrapper(ui_main)
    