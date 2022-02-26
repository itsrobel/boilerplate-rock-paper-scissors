from cgi import print_directory
import random
from collections import Counter
import pandas as pd

# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
rps_index = {"R": "P", "P": "S", "S": "R"}


def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    play_order = [{
        "RR": 0,
        "RP": 0,
        "RS": 0,
        "PR": 0,
        "PP": 0,
        "PS": 0,
        "SR": 0,
        "SP": 0,
        "SS": 0,
    }]
    df = pd.DataFrame({"History": opponent_history})
    # print(df.value_counts().max())
    df = df.value_counts()
    # print(df.idxmax()[0])

    # df1 = pd.DataFrame(data=df['History'].value_counts(),
    #                    columns=[['History', 'Count']])
    # guess = random.choice(['R', 'P', 'S'])
    guess = "R"
    style = random.randint(0, 1)
    if len(opponent_history) > 3:
        if style == 1:
            guess = opponent_history[-1]
            guess = rps_index[guess]
        if style == 0:

            guess = opponent_history[-1]
            guess = rps_index[guess]

            last_two = "".join(opponent_history[-2:])
            if len(last_two) == 2:
                play_order[0][last_two] += 1

            potential_plays = [
                prev_play + "R",
                prev_play + "P",
                prev_play + "S",
            ]
    # print(potential_plays)
            sub_order = {
                k: play_order[0][k]
                for k in potential_plays if k in play_order[0]
            }

            prediction = max(sub_order, key=sub_order.get)[-1:]
            guess = prediction
    # print(opponent_history[-2:])
    # print(guess)
    # print(opponent_history)

    return guess
