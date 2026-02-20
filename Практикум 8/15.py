ans=input()
print('\n' *25)

for _ in range(10):
    attempt=input()
    bulls=sum(a==b for a,b in zip(ans,attempt))
    cows=sum(ch in ans for ch in attempt)-bulls
    print("Быков:", bulls, "Коровов:", cows)
    if attempt==ans:
        print('Победа!')
        break
else:print('Проигрыш!')