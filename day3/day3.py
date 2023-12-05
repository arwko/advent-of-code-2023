import regex as re


def part_one():
    sum_numbers = 0
    with open("input") as file:
        # Find symbols used
        symbols = set(re.findall(r"[^\.^\d^\n]", file.read()))
        sym_pattern = r"["
        for s in symbols:
            sym_pattern += s + r"|"
        sym_pattern = sym_pattern[:-1] + r"]+"

        # Read all lines in input
        file.seek(0, 0)
        lines = file.read().splitlines()
        cols = len(lines[1])
        # Add frame with '.' around original input to avoid boundary checks
        input_expanded = []
        input_expanded.append("." * (cols + 2))
        for s in lines:
            input_expanded.append("." + s + ".")
        input_expanded.append("." * (cols + 2))

        for i in range(len(input_expanded)):
            matches = re.finditer(r"\d+", input_expanded[i])
            for m in matches:
                if (
                    re.search(
                        sym_pattern, input_expanded[i - 1][m.start() - 1 : m.end() + 1]
                    )
                    or re.search(
                        sym_pattern, input_expanded[i + 1][m.start() - 1 : m.end() + 1]
                    )
                    or re.match(sym_pattern, input_expanded[i][m.start() - 1])
                    or re.match(sym_pattern, input_expanded[i][m.end()])
                ):
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
    symbols = part_two()
