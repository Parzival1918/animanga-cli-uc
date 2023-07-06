def main():
    #imports
    import argparse

    #parser
    parser = argparse.ArgumentParser(description='Search for anime and manga using the command line.')
    #group = parser.add_mutually_exclusive_group()

    #arguments
    parser.add_argument('-t', '--type', choices=['cli', 'ui'], help='How to use the program. cli for command line interface, ui for user interface.', required=True)

    #parse
    args = parser.parse_args()

    #Check the arguments
    if args.type == 'cli':
        #imports
        from . import run_cli
        # print('cli')

        run_cli.main()
    elif args.type == 'ui':
        #imports
        from . import run_curses
        # print('ui')

        run_curses.main()

    pass

if __name__ == '__main__':
    main()