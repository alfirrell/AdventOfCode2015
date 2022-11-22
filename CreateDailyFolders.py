import os

for i in range(25):
    day_num = i + 1
    dir_name = "Day" + str(day_num).zfill(2)
    os.makedirs(dir_name, exist_ok=True)

    with open(dir_name + '/Exercise.md', 'w') as f:
        f.write('https://adventofcode.com/2022/day/' + str(day_num))
        f.write('\n\n')
        f.write('## Placeholder for today''s exercise\n')
