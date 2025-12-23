with open("input.txt") as f:
    data = f.read().strip().splitlines()

pos_start = 50
count_zero = 0
pos_cur = pos_start

for item in data:
    direction = item[0]
    num = int(item[1:])
    sign = -1 if direction == 'L' else 1
    while num > 0:
        pos_cur = pos_cur + sign
        if pos_cur % 100 == 0:
            count_zero += 1
        num -= 1

print(count_zero)


