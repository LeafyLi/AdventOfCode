from collections import defaultdict
with open('input.txt') as lines:
    lines = sorted([int(x.strip()) for x in lines.readlines()])

delta_of_one = delta_of_three = cur_jolts = 0
for next_jolt in lines:
    jolt_diff = next_jolt - cur_jolts
    if jolt_diff == 1:
        delta_of_one += 1
    elif jolt_diff == 3:
        delta_of_three += 1
    cur_jolts = next_jolt

#print(delta_of_one * (delta_of_three + 1))


# Go backwards
# memo_table[jolt] = how many ways to get to our charger from there
memo_table = defaultdict(int)
memo_table[lines[-1]] = 1
for joltage in reversed([0] + lines):
    if joltage + 1 in memo_table:
        memo_table[joltage] += memo_table[joltage + 1]
    if joltage + 2 in memo_table:
        memo_table[joltage] += memo_table[joltage + 2]
    if joltage + 3 in memo_table:
        memo_table[joltage] += memo_table[joltage + 3]
print(memo_table[0])



