import re


def part_one():
    sum_numbers = 0
    with open("input") as file:
        # Find symbols used

        # Read all lines in input
        lines = file.read().splitlines()
        cols = len(lines[1])
        # Add frame with '.' around original input to avoid boundary checks
        input_expanded = []
        input_expanded.append("." * (cols + 2))
        for s in lines:
            input_expanded.append("." + s + ".")
        input_expanded.append("." * (cols + 2))

        for r, lines in enumerate(input_expanded):
            print(f"{r} : {lines}")
            matches = re.finditer(r"\d+", lines)
            for m in matches:
                search_space = ""
                for row in range(r - 1, r + 2):
                    search_space += input_expanded[row][m.start() - 1 : m.end() + 1]
                if re.search(r"[^\.^\d^\n]", search_space):
                    sum_numbers += int(m.group())

    print(sum_numbers)


def part_two():
    with open("input") as file:
        lines = file.read().splitlines()
        cols = len(lines[1])
        # Add frame with '.' around original input to avoid boundary checks
        input_expanded = []
        input_expanded.append("." * (cols + 2))
        for s in lines:
            input_expanded.append("." + s + ".")
        input_expanded.append("." * (cols + 2))
        # convertback to single string for simpler search logic
        inp_str = "".join(input_expanded)
        # print(inp_str)
        cogs = re.finditer(r"\*", inp_str)
        for m in cogs:
            print(m)


def test_method():
    # part_one()
    part_two()


if __name__ == "__main__":
    symbols = part_one()
