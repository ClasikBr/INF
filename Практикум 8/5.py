st_1=input()
st_2=input()
st_3=input()
for ch in set(st_1+st_2+st_3):
    if (ch in st_1)+(ch in st_2)+(ch in st_3)==1:
        print(ch)