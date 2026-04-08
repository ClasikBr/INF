text = input()
words = [w.strip('.,!?;:-"\'()').lower() for w in text.split()]
print(list(set(words)))