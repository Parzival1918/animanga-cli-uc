#Handle calling Jikan API

import jikanpy
import time

jikan = jikanpy.Jikan()

# MUST HANDLE PAGINATION WITHOUT GOING OVER RATE LIMIT

def search(callpath: str, query: str, page=1):
    return [jikan.search(callpath, query, page=page)]

def seasonal(callpath: str, year: int = None, season: str = None):
    if callpath == 'anime':

        results = []
        page = 1
        while True:
            if year is None and season is None:
                result = jikan.seasons(extension='now', page=page)
            else:
                result = jikan.seasons(year=year, season=season, page=page)
                
            results.append(result)
            if not result['pagination']['has_next_page']:
               break

            #wait x seconds to avoid rate limit
            time.sleep(0.5)

            page += 1

        return results
    
def random(type: str):
    return jikan.random(type=type)

def schedule(day: str):
    return [jikan.schedules(day="day", parameters={'filter': day})] # Does not seem to get the day you ask for

def top(type: str, filter: str = None):
    return [jikan.top(type=type, parameters={'type': filter})]