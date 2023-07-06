#Handle calling Jikan API

import jikanpy

def searchAnime(query, page=1):
    jikan = jikanpy.Jikan()
    return jikan.search('anime', query, page=page)