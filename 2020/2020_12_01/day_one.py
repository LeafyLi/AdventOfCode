import itertools

with open("input.txt") as f:
    lines = [int(x) for x in f.readlines()]


def get_two_sum_multiplication(expenses, target_sum=2020):
    targets = {}
    for expense in expenses:
        targets[target_sum-expense] = expense
        if expense in targets:
            return expense, targets[expense]


val1, val2 = get_two_sum_multiplication(lines)
print(val1*val2)


def get_three_sum_multiplication(expenses):
    two_sum_targets = {2020-x: x for x in expenses}
    for target, first_val in two_sum_targets.items():
        two_sum_multiplication = get_two_sum_multiplication(expenses, target)
        if two_sum_multiplication is not None:
            return first_val * two_sum_multiplication[0] * two_sum_multiplication[1]


print(get_three_sum_multiplication(lines))

