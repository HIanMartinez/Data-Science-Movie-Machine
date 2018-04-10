import pandas as pd
import json
import urllib
import requests
import datetime
import os.path
from os.path import exists

from key import key

# You'll want to use an IMDb dataset so that it can match the IMDb title ID

def omdb_scraper(df):
    '''Will take in a dataset from IMDb to interact with the OMDb API.
    
    The function is built to recognize the tconst (title ID) column in
    an IMDb dataset.
    
    Returns: A .csv of movies with the:
    -Movie Title
    -Actors
    -Director
    -Awards
    -Box Office Returns
    -Country of Origin
    -Genre
    -Language
    -Metacritic Score
    -Short plot details
    -Production Studio
    -MPAA Rating
    -Rotten Tomatoes Score
    -Release Date
    -Runtime
    -Writer
    -Year (only) of release
    -Original IMDb ID
    -IMDb score
    
    Returns: A .csv of errors that may have occured.
    '''
    errors_list=[]
    for num, id in enumerate(df['tconst']):
        url = 'http://www.omdbapi.com/?apikey='+key+'&i='+str(id)
        response = requests.get(url)
        if response.status_code == 200:
            try:
                # If there's any reason that this would fail and cause the API caller to crash, this will instead
                # pass over the problematic entry
                data = json.loads(response.text)
                # This ensures that only valid omdb requests are parsed through
                if data['Response'] == 'True':
                    # This is to filter out any non-movie media (such as television series)
                    if data['Type'] == 'movie':
                        # This line should only pull requests that have had theater screenings
                        if data['BoxOffice'] !='N/A':
                            # In case there's a blank field for an entry (prevalent with overseas Rotten Tomatoes scores)
                            # these will try to find the data, if it isn't there, rather than crashing,
                            # it will pass in a null value
                            try:
                                actors = data['Actors']
                            except:
                                actors = 'Null'
                            try:
                                awards = data['Awards']
                            except:
                                awards = 'Null'
                            boxOffice = data['BoxOffice']
                            try:
                                country = data['Country']
                            except:
                                country = 'Null'
                            try:
                                genre = data['Genre']
                            except:
                                genre = 'Null'
                            try:
                                language = data['Language']
                            except:
                                language = 'Null'
                            try:
                                metacritic = data['Metascore']
                            except:
                                metacritic = 'Null'
                            try:
                                plot = data['Plot']
                            except:
                                plot = 'Null'
                            try:
                                production = data['Production']
                            except:
                                production = 'Null'
                            try:
                                rating = data['Rated']
                            except:
                                raint = 'Null'       
                            try:
                                rtscore = data['Ratings'][1]['Value']
                            except IndexError:
                                rtscore = 'N/A'
                            try:
                                release = data['Released']
                            except:
                                release = 'Null'
                            try:
                                runtime = data['Runtime']
                            except:
                                runtime = 'Null'
                            try:
                                title = data['Title']
                            except:
                                pass
                            try:
                                writer = data['Writer']
                            except:
                                writer = 'Null'
                            try:
                                director = data['Director']
                            except:
                                director = 'Null'
                            try:
                                year = data['Year']
                            except:
                                year = 'Null'
                            imdb_id = data['imdbID']
                            imdbscore = data['imdbRating']

                            # Creates a DataFrame to be filled with the items I'm requesting
                            raw_movies = pd.DataFrame(columns={ 'Movie Title','Actors', 'Director','Awards','Box Office ($)','Country','Genre', 
                                                               'Language', 'Metacritic Score', 'Plot', 'Production Studio', 'MPAA Rating',
                                                               'Rotten Tomatoes Score', 'Release Date', 'Runtime',
                                                               'Writer', 'Year of Release', 'imdb ID', 'imdb Score'})
                            raw_dataframe = pd.DataFrame({'Movie Title':title,'Actors': actors,'Director': director, 'Awards':awards, 
                                                          'Box Office ($)':boxOffice, 'Country': country, 'Genre':genre, 'Language':language, 
                                                          'Metacritic Score':metacritic, 'Plot':plot, 'Production Studio':production, 
                                                          'MPAA Rating':rating, 'Rotten Tomatoes Score':rtscore, 'Release Date':release, 
                                                          'Runtime':runtime, 'Writer':writer, 'Year of Release':year,
                                                          'imdb ID':imdb_id, 'imdb Score':imdbscore}, index=[0])
                            raw_movies = raw_movies.append(raw_dataframe)
                            raw_movies.to_csv('imdb_X.csv', mode='a', header=(not os.path.exists('./imdb_X.csv')))
                            if num % 500 == 0:                 
                                print(num)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            except:
                pass
        # If the request fails (because of a timeout or the site crashes), this will tell us where the crash occured
        # and create a csv so that we can return to it at a future point
        else:
            print('Call failed at request: ', num, response.status_code)
            errors_list.append((num, url, response.status_code))
            imdb_data_errors = pd.DataFrame(errors_list)
            imdb_data_errors.to_csv('imdb_data_errors.csv', mode='a')
