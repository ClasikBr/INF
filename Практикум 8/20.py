u = ["","один","два","три","четыре","пять","шесть","семь","восемь","девять"]
uf = ["","одна","две","три","четыре","пять","шесть","семь","восемь","девять"]
t10 = ["десять","одиннадцать","двенадцать","тринадцать","четырнадцать",
       "пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать"]
t = ["","", "двадцать","тридцать","сорок","пятьдесят","шестьдесят",
     "семьдесят","восемьдесят","девяносто"]
h = ["","сто","двести","триста","четыреста","пятьсот",
     "шестьсот","семьсот","восемьсот","девятьсот"]

def three(n, female=False):
    res = []
    res.append(h[n//100])
    x = n % 100
    if 10 <= x <= 19:
        res.append(t10[x-10])
        return " ".join([w for w in res if w])
    res.append(t[x//10])
    ulist = uf if female else u
    res.append(ulist[x%10])
    return " ".join([w for w in res if w])

def form(n, a, b, c):
    if n % 10 == 1 and n % 100 != 11: return a
    if 2 <= n % 10 <= 4 and not (12 <= n % 100 <= 14): return b
    return c

def num_to_words(n):
    if n == 0: return "ноль"
    mil = n // 1_000_000
    th = (n // 1000) % 1000
    r = n % 1000
    out = []
    if mil:
        out.append(three(mil))
        out.append(form(mil, "миллион", "миллиона", "миллионов"))
    if th:
        out.append(three(th, True))
        out.append(form(th, "тысяча", "тысячи", "тысяч"))
    if r:
        out.append(three(r))
    return " ".join(out)

n = int(input())
print(num_to_words(n))
