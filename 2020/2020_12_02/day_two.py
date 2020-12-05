processed_lines = []  # Tuple of (low, high, letter, password)
with open('input.txt') as f:
    for line in f:
        policy, password = line.split(':')
        password = password.strip()
        policy = policy.strip()
        count_range, letter = policy.split(' ')
        low, high = [int(x) for x in count_range.split('-')]
        processed_lines.append((low, high, letter, password))


valid_passwords = 0
for low, high, letter, password in processed_lines:
    valid_passwords += low <= password.count(letter) <= high

print(valid_passwords)



valid_passwords = 0
for low, high, letter, password in processed_lines:
    valid_passwords += (password[low-1] == letter) ^ (password[high-1] == letter)

print(valid_passwords)
