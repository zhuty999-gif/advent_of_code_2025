with open("input.txt") as f:
    data = f.read().strip().splitlines()

pos_start = 50
count_zero = 0
pos_cur = pos_start

for item in data:
    direction = item[0]
    num = int(item[1:])
    if direction == 'L':
        pos_cur = (pos_cur - num)
    elif direction == 'R':
        pos_cur = (pos_cur + num)
    if pos_cur % 100 == 0:
        count_zero += 1

print(count_zero)


