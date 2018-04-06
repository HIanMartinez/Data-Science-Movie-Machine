import pandas as pd
import json
import urllib
import requests
from pandas.io.json import json_normalize
import re
from key import key

imdb_df = pd.read_csv('./title.ratings.tsv',  sep='\t', header=0)

errors_list=[]
results_list=[]
for num, id in enumerate(imdb_df['tconst'][100000:]):
    url = 'http://www.omdbapi.com/?apikey='+key+'&i='+str(id)
    response = requests.get(url)
    if response.status_code == 200:
        results_list.append(response.json())
        if num % 500 == 0:
            imdb_dataX = pd.DataFrame(results_list)
            imdb_dataX.to_csv('imdb_dataX.csv',mode='a')
        if num % 500 == 0:
            print(num)
    else:
	print('Call failed at request: ', num, response.status_code)
        errors_list.append((num, url, response.status_code))
        if num % 500 == 0:
            imdb_data_errors = pd.DataFrame(errors_list)
            imdb_data_errors.to_csv('imdb_data_errors.csv', mode='a')

imdb_df = pd.read_csv('./title.ratings.tsv',  sep='\t', header=0)


results_list=[]
for num, id in enumerate(imdb_df['tconst'][:50000]):    
    url = 'http://www.omdbapi.com/?apikey='+key+'&i='+str(id)
    response = requests.get(url)
    if response.status_code == 200:
        results_list.append(response.json())
        if num % 500 == 0:
            print(num)
    else:
        print('Call failed at request: ', num, response.status_code)
        

