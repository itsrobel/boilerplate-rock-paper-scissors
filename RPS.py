from cgi import print_directory
import random
from collections import Counter
from matplotlib.pyplot import axes, axis
import pandas as pd
from RPS_game import abbey, mrugesh
from itertools import permutations
from itertools import product
import operator

from beatAbbey import beatAbbey
# The example

# unction below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
rps_index = {"R": "P", "P": "S", "S": "R"}


def player(prev_play, opponent_history=[]):
    list_rps = (get_perm("RPS", 3))
    df_play = pd.DataFrame(list_rps, columns=["play", "value"])

    opponent_history.append(prev_play)
    opponent_hist_str = "".join(opponent_history)

    df_new = find_and_sort(df_play, opponent_hist_str)
    next_play = select_rank(df_new, opponent_history)
    if len(opponent_history) < 2:
        next_play = "P"
        # print(opponent_history)
    abbey = beatAbbey(prev_play)

    if len(opponent_history) > 1000 & len(opponent_history) < 2000:
        return abbey
    else:
        return rps_index[next_play]
    # elif rn == 3 | rn == 2:
    #     return abbey(prev_play)
    # elif rn < 4:
    #     return mrugesh(prev_opponent_play=prev_play)


def get_perm(str1, rno):
    chars = list(str1)
    results = []
    for c in product(chars, repeat=rno):
        results.append(["".join(list(c)), 0])
    return results


def find_and_sort(df, string):
    def count(play, value):
        value = string.count(play)
        return value
    df['value'] = df.apply(lambda row: count(
        row['play'], row['value']), axis=1)
    return df


def select_rank(df, hist):
    hist = "".join(hist[-2:])

    def find(play):
        if hist in play[:2]:
            return play

    df['play'] = df.apply(lambda row: find(row["play"]), axis=1)
    dist = (df[df["play"].notnull()])
    play = dist['value'].idxmax()

    # print(df)
    # print(hist)
    play = dist.loc[play]['play'][-1:]
    # print(play)
    return play
