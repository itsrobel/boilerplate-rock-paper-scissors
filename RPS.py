import pandas as pd
from itertools import product

from beatAbbey import beatAbbey
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
    abbey = beatAbbey(prev_play)

    if len(opponent_history) > 1000 & len(opponent_history) < 2000:
        return abbey
    else:
        return rps_index[next_play]


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
    play = dist.loc[play]['play'][-1:]
    return play
