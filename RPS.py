from cgi import print_directory
import random
from collections import Counter
import pandas as pd
from RPS_game import abbey
from itertools import permutations
from itertools import product
import operator
# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
rps_index = {"R": "P", "P": "S", "S": "R"}


def player(prev_play, opponent_history=[]):
    dict_rps= get_perm("RPS", 3)
    df_play=pd.DataFrame.from_dict(dict_rps,  orient='index',  columns=['value'])
    df_play.index.name = "key"


    if not prev_play:
        prev_play = 'R'
    
    opponent_history.append(prev_play)
    # print(df_play.index.name)
    opponent_hist_str = "".join(opponent_history)

    find_and_sort(df_play, opponent_hist_str)
    # print(df_play.sort_values(by="value",ascending=False))
    # print(df_play)
    # df_play[]
    # for i in df_play:
    #     df_play["value"] = ohs.count(df_play["key"])
    # print(df_play)
    # print(max(df_play, key=operator.itemgetter(1)))
    return abbey(prev_opponent_play=prev_play)

def get_perm(str1, rno):
  chars = list(str1)
  results = {}
  for c in product(chars, repeat = rno):
    results["".join(list(c))] = 0
  return results

def find_and_sort(df, string):
    for index, row in df.iterrows():
        # print(index)
        # print(string.count(index))
        # print(row['value'])
        row['value'] = string.count(index)

    df = (df.sort_values(by="value",ascending=False))

    return df