import re
from collections import defaultdict


def part_one() -> None:
    sum_val = 0
    tot_num_cards = 219
    copies = defaultdict(int)
    with open("input") as f:
        for ln, line in enumerate(f):
            winners = re.search(r"(?<=:)(\s+\d+){10}", line).group().split()
            numbers = re.search(r"(?<=|)(\s+\d+){25}", line).group().split()
            num_winners_chosen = len(set(numbers).intersection(set(winners)))
            # Part 1
            if num_winners_chosen > 0:
                sum_val += 2 ** (num_winners_chosen - 1)
            # Part 2
            copies[ln] += 1
            print(copies[ln])
            if num_winners_chosen > 0:
                for s in range(ln + 1, ln + 1 + num_winners_chosen + 1):
                    if s < tot_num_cards - 1:
                        copies[s] += copies[ln]
    print(sum_val)
    # print(copies.total())


if __name__ == "__main__":
    part_one()
