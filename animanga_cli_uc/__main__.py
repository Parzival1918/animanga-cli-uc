def main():
    #imports
    import argparse
    from . import run_cli

    #parser
    parser = argparse.ArgumentParser(description='Search for anime and manga using the command line.', prog='animanga')
    subparsers = parser.add_subparsers(help='sub-command help', required=True)

    #arguments
    #ANIME
    parser_A = subparsers.add_parser('anime', help='Fetch anime data.')
    parser_A.set_defaults(which='anime')
    subparser_A = parser_A.add_subparsers(help='sub-command help')

    parser_A_query = subparser_A.add_parser('search', help='Search anime by name.')
    parser_A_query.set_defaults(which='anime/search')
    parser_A_query.add_argument('-q', '--query', help='Search query.')

    parser_A_seasonal = subparser_A.add_parser('seasonal', help='Fetch seasonal anime by year and season.')
    parser_A_seasonal.set_defaults(which='anime/seasonal')
    parser_A_seasonal.add_argument('--current', help='Anime from current season', action='store_true')
    parser_A_seasonal.add_argument('-y', '--year', help='Year.', type=int)
    parser_A_seasonal.add_argument('-e', '--season', help='Season.', choices=['winter', 'spring', 'summer', 'fall'])

    #MANGA
    parser_M = subparsers.add_parser('manga', help='Fetch manga data.')
    parser_M.set_defaults(which='manga')
    group_M = parser_M.add_mutually_exclusive_group(required=True)
    group_M.add_argument('-q', '--query', help='Search query.')

    #parse
    args = parser.parse_args()

    print(args)

    run_cli.main(args=args)

if __name__ == '__main__':
    main()