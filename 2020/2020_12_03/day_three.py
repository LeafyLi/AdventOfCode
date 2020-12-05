import itertools
import operator

with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

print(len(lines[0]), len(lines))


def get_num_trees_for_slope(d_x, d_y):
    num_trees = 0
    location = 0, 0
    while location[0] < len(lines):
        num_trees += lines[location[0]][location[1]] == "#"
        location = location[0] + d_y, (location[1] + d_x) % 31
    return num_trees

pairs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(list(itertools.accumulate([get_num_trees_for_slope(d_x, d_y) for d_x, d_y in pairs], operator.mul))[-1])