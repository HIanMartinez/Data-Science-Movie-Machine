import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle

def predict_monies(*args):
    '''
    All inputs should be strings
    
    -Input Actor/Actress names
    -Input Genre choice
    -Input Director name
    '''
    new_df1 = pd.read_csv("bop.csv", index_col=0)
    rf_act = pd.read_pickle("rf_act.p")
    lst = [arg.lower() for arg in args]
    for i in lst:
        new_df1[i] = 1.0
    result1 = rf_act.predict(new_df1.drop('Box Office ($)', axis = 1))/1000000
    result1 = str(result1)
    result1 = result1.replace('[', '')
    result1 = result1.replace(']', '')
    print("Your film idea is predicted to return "+str(result1)[0:4]+"M dollars!")