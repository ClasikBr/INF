def count_letters(sentence: str) -> None:
    vow = 'аеёиоуыэюя'
    cons = 'бвгджзйклмнпрстфхцчшщъь'

    s = sentence.lower()
    v = sum(ch in vow for ch in s)
    c = sum(ch in cons for ch in s)

    print(f"Гласных: {v}, Согласных: {c}")
