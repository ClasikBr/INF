a,b=map(int,input().split('x'))
a,b=sorted((a,b))
c,d,e=map(int,input().split('x'))
faces=[sorted((c,d)), sorted((c,e)), sorted((d,e))]
print('да' if any(f[0]<=a and f[1]<=b for f in faces) else 'нет')