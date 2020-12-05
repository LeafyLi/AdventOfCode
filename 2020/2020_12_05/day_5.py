with open('input.txt') as f:
    passes = [x.strip() for x in f.readlines()]

seat_ids = []
for seat in passes:
    seat_binary = seat.translate(seat.maketrans('FBLR', '0101'))
    seat_val = int(seat_binary, 2)
    seat_ids.append(seat_val)

print(max(seat_ids))

print(set([x for x in range(127*8 + 8) if min(seat_ids) <= x <= max(seat_ids)]) - set(seat_ids))

