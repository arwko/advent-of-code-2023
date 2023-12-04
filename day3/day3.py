import regex as re


def find_symbols() -> list:
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
        rows = len(lines)
        cols = len(lines[1])
        # Add frame with '.' around original input to avoid boundary checks
        input_expanded = []
        input_expanded.append("." * (cols + 2))
        for s in lines:
            input_expanded.append("." + s + ".")
        input_expanded.append("." * (cols + 2))

        for i in range(len(input_expanded)):
            print(str(i) + ": ", end="")
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
                    print(int(m.group()), end=",")
                    sum_numbers += int(m.group())
            print("\n")

    print(sum_numbers)
    return list(symbols)


def test_method():
    find_symbols()


if __name__ == "__main__":
    symbols = find_symbols()
