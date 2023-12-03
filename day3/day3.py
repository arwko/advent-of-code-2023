import regex as re


def find_symbols() -> list:
    with open("input") as file:
        # Find symbols used
        symbols = set(re.findall(r"[^\.^\d^\n]", file.read()))
        print(list(symbols))

        # Read all lines in input
        file.seek(0, 0)
        lines = file.readlines()
        rows = len(lines)
        cols = len(lines[1])
        print("Rows: " + str(rows) + ", Cols: " + str(cols))
        # Add frame with '.' around original input to avoid boundary checks
        input_expanded = []
        input_expanded.append("." * (cols + 2))
        for s in lines:
            input_expanded.append("." + s + ".")
        input_expanded.append("." * (cols + 2))

        for i in range(1, rows + 1):
            matches = re.finditer(r"\d+", input_expanded[i])
            for match in matches:
    #                if re.search()
                pass

    return list(symbols)


    if __name__ == "__main__":
    symbols = find_symbols()
