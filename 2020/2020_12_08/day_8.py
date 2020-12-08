with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]


def process_line(line):
    op, number = line.split(' ')
    sign, abs_val = number[0], int(number[1:])
    return op, sign, abs_val


def exec_lines(lines):
    executed_indices = set()
    i = accumulator_val = 0
    while True:
        if i >= len(lines):
            return 'success', accumulator_val, _
        op, sign, abs_val = process_line(lines[i])
        if i in executed_indices:
            return None, None, executed_indices
        executed_indices.add(i)
        if op == 'acc':
            if sign == '+':
                accumulator_val += abs_val
            elif sign == '-':
                accumulator_val -= abs_val
            else:
                raise ValueError(f'Invalid sign {accumulator_val}')
            i += 1
        elif op == 'nop':
            i += 1
        elif op == 'jmp':
            if sign == '+':
                i += abs_val
            elif sign == '-':
                i -= abs_val
        else:
            raise ValueError(f'Invalid op {op} ')


_, accumulator_val, executed_indices = exec_lines(lines)
print(accumulator_val)




# pt 2
for orig_idx in executed_indices:
    op, sign, abs_val = process_line(lines[orig_idx])
    if op in ['nop', 'jmp']:
        if op == 'nop':
            switched_op = 'jmp'
        elif op == 'jmp':
            switched_op = 'nop'
        candidate_lines = list(lines)
        candidate_lines[orig_idx] = ' '.join([switched_op, sign + str(abs_val)])
        status, accumulator_val, _ = exec_lines(candidate_lines)
        if status == 'success':
            print(accumulator_val)
            break
