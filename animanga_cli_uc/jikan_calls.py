#Handle calling Jikan API

import jikanpy
import time

jikan = jikanpy.Jikan()

def search(callpath: str, query: str, page=1):
    return jikan.search(callpath, query, page=page)

def seasonal(callpath: str):
    if callpath == 'anime':

        results = []
        page = 1
        while True:
            result = jikan.seasons(extension='now', page=page)
            results.append(result)
            if not result['pagination']['has_next_page']:
               break

            #wait x seconds to avoid rate limit
            time.sleep(0.5)

            page += 1

        return results