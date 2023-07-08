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

    parser_A_recommendations = subparser_A.add_parser('recommendations', help='Fetch anime recommendations.')
    parser_A_recommendations.set_defaults(which='anime/recommendations')

    parser_A_top = subparser_A.add_parser('top', help='Fetch anime top.')
    parser_A_top.set_defaults(which='anime/top')
    parser_A_top.add_argument('type', help='Filter top search.', choices=['upcoming', 'tv', 'movie', 'ova'])

    parser_A_shedule = subparser_A.add_parser('schedule', help='Fetch anime schedule.')
    parser_A_shedule.set_defaults(which='schedule')
    parser_A_shedule.add_argument('day', help='Day of the week.', choices=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])

    parser_A_random = subparser_A.add_parser('random', help='Fetch random anime.')
    parser_A_random.set_defaults(which='anime/random')

    #MANGA
    parser_M = subparsers.add_parser('manga', help='Fetch manga data.')
    parser_M.set_defaults(which='manga')
    group_M = parser_M.add_mutually_exclusive_group(required=True)
    group_M.add_argument('-q', '--query', help='Search query.')

    #CHARACTERS
    parser_C = subparsers.add_parser('characters', help='Fetch character data.')
    parser_C.set_defaults(which='characters')
    subparser_C = parser_C.add_subparsers(help='sub-command help')

    parser_C_search = subparser_C.add_parser('search', help='Search characters by name or id.')
    parser_C_search.set_defaults(which='characters/search')
    search_or_id = parser_C_search.add_mutually_exclusive_group(required=True)
    search_or_id.add_argument('--query', help='Search query.')
    search_or_id.add_argument('--id', help='Character MAL id.')

    parser_C_random = subparser_C.add_parser('random', help='Fetch random characters.')
    parser_C_random.set_defaults(which='characters/random')

    parser_C_top = subparser_C.add_parser('top', help='Fetch top characters.')
    parser_C_top.set_defaults(which='characters/top')
    

    #RANDOM
    # parser_R = subparsers.add_parser('random', help='Fetch random anime, manga and more.')
    # parser_R.set_defaults(which='random')
    # parser_R.add_argument('type', help='Type of random data.', choices=['anime', 'manga', 'characters', 'people', 'users'])

    #parse
    args = parser.parse_args()

    print(args)

    run_cli.main(args=args)

if __name__ == '__main__':
    main()