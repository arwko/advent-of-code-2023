def hash_f(input: str) -> int:
    hash = 0
    for c in input:
        hash += ord(c)
        hash *= 17
        hash = hash % 256
    # print(input)
    print(hash)

    return hash


if __name__ == "__main__":
    with open("input") as f:
        instructions = f.read().strip().split(",")
        sum = 0
        for i in instructions:
            sum += hash_f(i)

        print(sum)
