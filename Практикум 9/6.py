def write_fout(message: str) -> None:
    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(message)


with open('input.txt', 'r', encoding='utf-8') as fin:
    lines = fin.readlines()

try:
    f_line = int(lines[0].strip())
except ValueError:
    write_fout('ERROR')
else:
    ct = len(lines) - 1
    if ct == f_line:
        write_fout('YES')
    else:
        write_fout('NO')
