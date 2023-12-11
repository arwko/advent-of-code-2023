import pandas as pd
from collections import Counter

def value(hand : str, replace_joker: bool) -> int:
    c = Counter(hand)
    if replace_joker:
        if c['J'] > 0 and c['J'] < 5 and c.most_common()[0][0] != 'J':
            # Increase the card with highest count
            c[c.most_common()[0][0]] += c['J']
            del c['J']
    
    match c.most_common()[0][1]:
        case 1:
            # Only high card
            return 1
        case 2:
            # Single Pair or double pair
            if c.most_common()[1][1] == 1:
                return 2
            else:
                return 3
        case 3:
            # Three of a kind or full house
            if c.most_common()[1][1] == 1:
                return 4
            else:
                return 5
        case 4:
            # Four of a kind
            return 6
        case 5:
            # Five of a kind
            return 7
    

def value_list(hands : list, replace_joker : bool) -> list:
    values = []
    for h in hands:
        values.append(value(h, replace_joker))
    
    return values

def read_data(filename : str) -> pd.DataFrame:
    return pd.read_csv(filename, sep=' ',names=['hand','bid'])

def calculate_total_score(df : pd.DataFrame, repl_j: bool):
        # Calculate the rank of the hand
    df['rank'] = value_list(df['hand'], repl_j)
    # Replace letters to allow sorting
    df['hand'] = df['hand'].str.replace('A','E')
    df['hand'] = df['hand'].str.replace('K','D')
    df['hand'] = df['hand'].str.replace('Q','C')
    if repl_j:
        df['hand'] = df['hand'].str.replace('J','1')
    else:
        df['hand'] = df['hand'].str.replace('J','B')
    df['hand'] = df['hand'].str.replace('T','A')
    df.sort_values(by=['rank','hand'], inplace=True)
    df['multiplier'] = range(1,len(df)+1)
    df['score'] = df['bid']*df['multiplier']
    
    print(df.head())
    print(sum(df['score']))

if __name__ == '__main__':
    df = read_data('input')
    # Part one
    calculate_total_score(df, False)
    
    # Part two
    #calculate_total_score(df, True)

