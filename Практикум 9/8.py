days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = [
    "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
    "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
]

with open('input.txt', encoding = 'utf-8') as fin:
    data = [int(line.strip()) for line in fin]

avr = []
index = 0

for d in days:
    step = data[index:index + d]
    avr.append(sum(step) / d)
    index += d

with open('output.txt', 'w', encoding = 'utf-8') as fout:
    for month, ans in zip(months, avr):
        fout.write(f"{month}: {ans}\n")
