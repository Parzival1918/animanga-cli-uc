def main():
    #imports
    import argparse
    from . import run_cli

    #parser
    parser = argparse.ArgumentParser(description='Search for anime and manga using the command line.')
    subparsers = parser.add_subparsers(help='sub-command help', required=True)

    #arguments
    parser_A = subparsers.add_parser('anime', help='Fetch anime data.')
    parser_A.set_defaults(which='anime')
    group_A = parser_A.add_mutually_exclusive_group(required=True)
    group_A.add_argument('-q', '--query', help='Search query.')
    group_A.add_argument('-s', '--seasonal', help='Fetch seasonal anime.', action='store_true')

    parser_M = subparsers.add_parser('manga', help='Fetch manga data.')
    parser_M.set_defaults(which='manga')
    group_M = parser_M.add_mutually_exclusive_group(required=True)
    group_M.add_argument('-q', '--query', help='Search query.')
    group_M.add_argument('-s', '--seasonal', help='Fetch seasonal anime.', action='store_true')

    #parse
    args = parser.parse_args()

    # print(args)

    run_cli.main(args=args)

if __name__ == '__main__':
    main()