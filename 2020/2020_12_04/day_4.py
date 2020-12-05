with open('input.txt') as f:
    lines = f.readlines()


def is_valid_field(key: str, val: str) -> bool:
    if key == 'byr':
        return len(val) == 4 and 1920 <= int(val) <= 2002
    elif key == 'iyr':
        return len(val) == 4 and 2010 <= int(val) <= 2020
    elif key == 'eyr':
        return len(val) == 4 and 2020 <= int(val) <= 2030
    elif key == 'hgt':
        if not len(val) > 2:
            return False
        if val[-2:] == 'cm':
            return 150 <= int(val[:-2]) <= 193
        elif val[-2:] == 'in':
            return 59 <= int(val[:-2]) <= 76
        return False
    elif key == 'hcl':
        if not val:
            return False
        return len(val) == 7 and val[0] == '#' and all([x.isalnum() for x in val[1:]]) and \
               all([x.islower() for x in val[1:] if x.isalpha()])
    elif key == 'ecl':
        return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        val.lstrip('0')
        return len(val) == 9 and all([x.isnumeric() for x in val])
    return False


valid_passports = 0
required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

present_fields = set()
for idx, val in enumerate(lines):
    if val == '\n':
        valid_passports += present_fields == required_fields
        present_fields = set()
        continue
    fields = val.strip().split(' ')
    for field in fields:

        key, val = field.split(':')
        if key == 'cid':
            continue
        if is_valid_field(key, val):
            present_fields.add(key)
valid_passports += present_fields == required_fields
print(valid_passports)
