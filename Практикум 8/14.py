hint=input()
ans=input()
print('\n' *25)
masked=['*']*len(ans)
print(hint, ''.join(masked), sep='\n')
for _ in range(10):
    if input('Буква или слово (0 - буква, 1 - слово)?')=='0':
        ch=input()
        for i, c in enumerate(ans):
            if c==ch:
                masked[i]=ch
        print(''.join(masked))
        if ''.join(masked)==ans:
            print('Победа!')
            break
    else:
        print('Победа!' if input()==ans else 'Проигрыш!')
        break
else:print('Проигрыш!')