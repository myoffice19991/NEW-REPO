import random
import pandas as pd
import numpy as np

def play_game(name):
    # Game logic here
    j = 0
    m = 0
    s = 0
    streak = np.nan

    for i in range(3):
        a = random.randint(1, 3)
        ans = int(input("Guess a number: "))
        if a == ans:
            j += 1
            s += 1
            print("Bravo")
            if j == 2:
                streak = 'Classic'
                print(streak)
            if j == 3:
                print("")
                streak = 'KING OF KINGS'
                print(streak)
                break
        else:
            print("")
            print("Oh no!! I guessed", a)
            print(f"Try again......")
            m += 1
            if m == 3:
                print("")
                streak = 'LOOSSER'
                print(streak)

    return s, streak

def save_player_data(name, score, streak):
    # Save player data to CSV file
    try:
        df = pd.read_csv('player_data.csv')
    except FileNotFoundError:
        print("File not found.")
        df = pd.DataFrame(columns=['ID', 'Player Name', 'Score', 'Fame'])

    if name in df['Player Name'].values:
        player_id = df.loc[df['Player Name'] == name, 'ID'].iloc[0]
    else:
        if len(df) == 0:
            player_id = 1
        else:
            player_id = df['ID'].max() + 1

    new_record = {'ID': player_id, 'Player Name': name, 'Score': score, 'Fame': streak}
    df = df.append(new_record, ignore_index=True)
    df.to_csv('player_data.csv', index=False)
