import functools


with open('input.txt') as f:
    lines = f.readlines()


cur_group_declarations = set()
all_groups = []
for line in lines:
    if line == '\n':
        all_groups.append(cur_group_declarations)
        cur_group_declarations = set()
    else:
        cur_group_declarations = cur_group_declarations.union(set([x for x in line.strip()]))
if cur_group_declarations:
    all_groups.append(cur_group_declarations)


def set_len_accumulate(total, element):
    return total + len(element)


print(functools.reduce(set_len_accumulate, all_groups, 0))


# Pt 2
cur_group_declarations = []
all_groups = []
for line in lines:
    if line == '\n':
        all_groups.append(cur_group_declarations)
        cur_group_declarations = []
    else:
        cur_group_declarations.append(set([x for x in line.strip()]))
if cur_group_declarations:
    all_groups.append(cur_group_declarations)


def consensus_len_accumulate(total, element):
    return total + len(functools.reduce(set.intersection, element))


print(functools.reduce(consensus_len_accumulate, all_groups, 0))
