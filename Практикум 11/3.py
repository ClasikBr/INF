text = input()
words = [w.strip('.,!?;:-"\'()') for w in text.split()]
print(words)