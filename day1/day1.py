import re

def parse_input_p2(filename: str):
    sum_vals = 0
    conversion_table = {
            **dict.fromkeys(['one', '1'],'1'),
            **dict.fromkeys(['two', '2'], '2'),
            **dict.fromkeys(['three', '3'], '3'),
            **dict.fromkeys(['four', '4'], '4'),
            **dict.fromkeys(['five', '5'], '5'),
            **dict.fromkeys(['six', '6'], '6'),
            **dict.fromkeys(['seven', '7'], '7'),
            **dict.fromkeys(['eight', '8'], '8'),
            **dict.fromkeys(['nine', '9'], '9'),
            **dict.fromkeys(['zero', '0'], '0')
            }
    with open(filename) as f:
        for line in f:
            # Part 1
            #ints = re.findall(r'\d', line)
            #sum_vals += int(ints[0]+ints[-1])

            # Part 2
            ints = re.findall(r'(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))', line)
           
            sum_vals += int(conversion_table[ints[0]]+conversion_table[ints[-1]])
        print(sum_vals)

if __name__ == "__main__":
    parse_input_p2('input')
