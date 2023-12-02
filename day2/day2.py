import regex as re


def part_one_and_two():
    """Process input and find answers to both parts""" 
   
    max_nums = {'red': 12, 'green': 13, 'blue': 14}
    accumulator = 0
    accumulator2 = 0
    game_id = 1

    with open('input') as file:
        for line in file:
            game_ok = True
            mult = 1

            for key, val in max_nums.items():
                regex_p= r'\d+(?=\s' + re.escape(key) + r')'
                n_cubes = re.findall(regex_p,line)
                if any(int(t) > val for t in n_cubes):
                    game_ok = False
                mult *= max(int(t) for t in n_cubes)    
            if game_ok:
                accumulator += game_id

            game_id += 1
            accumulator2 += mult
    print('Part 1: ' + str(accumulator))
    print('Part 2: ' + str(accumulator2))


if __name__ == "__main__":
    part_one_and_two()
