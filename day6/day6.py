def part_one():
    with open('input') as file:
        times = [int(s) for s in file.readline().split()[1:]]
        dist_record = [int(s) for s in file.readline().split()[1:]]

    tot_val = 1
    for n, time in enumerate(times):
        num_ok = 0
        for t in range(0,time):
            a = t
            dist = a * (time-t)
            if dist > dist_record[n]:
                num_ok += 1
        tot_val *= num_ok

    print(tot_val)

def part_two():
    with open('input') as file:
        time = int(''.join(file.readline().split()[1:]))
        dist_record = int(''.join(file.readline().split()[1:]))
    num_ok = 0
    for t in range(0,time):
        a = t
        dist = a * (time-t)
        if dist > dist_record:
            num_ok += 1
    print(num_ok)
    

if __name__ == '__main__':
    part_one()
    part_two()