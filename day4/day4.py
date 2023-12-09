import re
from collections import defaultdict
from typing import Counter


def part_one(
    filename: str, num_winners: int, num_candidates: int, tot_num_cards
) -> None:
    sum_val = 0
    # copies = defaultdict(int)
    copies = Counter()
    with open(filename) as f:
        for ln, line in enumerate(f):
            # print(line)
            p1 = r"(?<=:)(\s+\d+){" + re.escape(str(num_winners)) + r"}"
            winner_str = re.search(p1, line)
            # if winner_str is not None:
            # winners = winner_str.group().split()
            winners = winner_str.group().split() if winner_str is not None else []
            p2 = r"(?<=|)(\s+\d+){" + re.escape(str(num_candidates)) + r"}"
            numbers_str = re.search(p2, line)
            # if numbers_str is not None:
            # numbers = numbers_str.group().split()
            numbers = numbers_str.group().split() if numbers_str is not None else []
            num_winners_chosen = len(set(numbers).intersection(set(winners)))
            # Part 1
            if num_winners_chosen > 0:
                sum_val += 2 ** (num_winners_chosen - 1)
            # Part 2
            copies[ln] += 1
            print(str(ln) + " : " + str(copies[ln]))
            print("Num winners: " + str(num_winners_chosen))
            if num_winners_chosen > 0:
                for s in range(ln + 1, ln + 1 + num_winners_chosen):
                    print("Increment " + str(s))
                    if s < tot_num_cards:
                        copies[s] += copies[ln]
    print("Part 1: " + str(sum_val))
    print("Part 2: " + str(copies.total()))
    print(copies)


if __name__ == "__main__":
    # part_one("test_input", 5, 8, 6)
    part_one("input", 10, 25, 219)
