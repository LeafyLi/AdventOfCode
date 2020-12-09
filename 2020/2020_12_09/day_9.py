from collections import deque

with open('input.txt') as f:
    f = [int(x.strip()) for x in f.readlines()]


def has_valid_two_sum(vals, target_sum):
    targets = {}
    for val in vals:
        targets[target_sum-val] = val
        if val in targets:
            return True
    return False


cur_vals = deque(f[:25], 25)

for i in range(25, len(f)):
    next_val = f[i]
    if not has_valid_two_sum(cur_vals, next_val):
        invalid_num = next_val
        print(next_val)
        break
    else:
        cur_vals.popleft()
        cur_vals.append(next_val)


# pt 2
# 133015568
for i in range(len(f)):
    for j in range(i+1, len(f)):
        if sum(f[i:j+1]) == 133015568:
            print(min(f[i:j+1]) + max(f[i:j+1]))
            break
