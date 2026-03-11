from pathlib import Path

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def date_of_year(date_str: str) -> int:
    day, month = map(int, date_str.split('.'))
    return sum(days[:month - 1]) + day

input_path = Path('input.txt')
output_path = Path('output.txt')

lines = input_path.read_text(encoding='utf-8').strip().splitlines()

cur_date = lines[0]
ct = int(lines[1])

cur_day = date_of_year(cur_date)

ans = []

for line in lines[2:2 + ct]:
    cell, date = line.split()
    stored_day = date_of_year(date)

    if cur_day - stored_day > 3:
        ans.append(cell)

output_path.write_text('\n'.join(ans) + '\n', encoding='utf-8')
