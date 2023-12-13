import numpy as np

sum = 0
sum2 = 0

with open('input') as f:
    for r, line in enumerate(f):
        iteration = 0
        vals = [int(s) for s in line.split()]
        next_val = vals[-1]
        prev_val = vals[0]
        while not np.all(vals == 0):
            vals = np.diff(vals)
            next_val += vals[-1]
            prev_val -= vals[0]*np.power(-1,iteration)
            iteration += 1
        sum += next_val
        sum2 += prev_val

print(sum) 
print(sum2)
