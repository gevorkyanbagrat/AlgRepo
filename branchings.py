def countUp(a,b):#1
    if a > b:
        c = a + b
    elif a == b:
        c = a * b
    else:
        c = a - b
    return c

def determineWhichQuarter(x,y):#2
    if (y > 0) and (x > 0):
        c = 'первая четверть'
    if (y > 0) and (x < 0):
        c = 'вторая четверть'
    if (y < 0) and (x < 0):
        c = 'третья четверть'
    if (y < 0) and (x > 0):
        c = 'четвертая четверть'
    return c

def outputInAscendingOrder(a,b,c):#3
    ans=[]
    if (a > b) and (a > c) and (b > c):
        ans.append(a)
        ans.append(b)
        ans.append(c)
    if (a > b) and (a > c) and (b < c):
        ans.append(a)
        ans.append(c)
        ans.append(b)
    if (b > a) and (b > c) and (a > c):
        ans.append(b)
        ans.append(a)
        ans.append(c)
    if (b > a) and (b > c) and (a < c):
        ans.append(b)
        ans.append(c)
        ans.append(a)
    if (c > a) and (c > b) and (a > b):
        ans.append(c)
        ans.append(a)
        ans.append(b)
    if (c > a) and (c > b) and (a < b):
        ans.append(c)
        ans.append(b)
        ans.append(a)
    return ans

def solveTheEquation(a,b,c):#4
    disc = b ** 2 + 4 * a * c
    x1 = round((b * (-1) + disc ** 0.5) / 2 * a, 2)
    x2 = round((b * (-1) - disc ** 0.5) / 2 * a, 2)
    return x1,x2

def outputLetterEntry(A):#5
    A = int(input())
    decade = A // 10
    unit = A % 10
    if (decade >= 2):
        if (decade == 2):
            B = "двадцать"
        if (decade == 3):
            B = "тридцать"
        if (decade == 4):
            B = "сорок"
        if (decade == 5):
            B = "пятьдесят"
        if (decade == 6):
            B = "шестьдесят"
        if (decade == 7):
            B = "семьдесят"
        if (decade == 8):
            B = "восемьдесят"
        if (decade == 9):
            B = "девяносто"
    elif (decade < 2):
        if (A == 10):
            B = "десять"
        if (A == 11):
            B = "одиннадцать"
        if (A == 12):
            B = "двенадцать"
        if (A == 13):
            B = "тринадцать"
        if (A == 14):
            B = "четырнадцать"
        if (A == 15):
            B = "пятнадцать"
        if (A == 16):
            B = "шестнадцать"
        if (A == 17):
            B = "семнадцать"
        if (A == 18):
            B = "восемнадцать"
        if (A == 19):
            B = "девятнадцать"
    if (unit == 1):
        C = "один"
    if (unit == 2):
        C = "два"
    if (unit == 3):
        C = "три"
    if (unit == 4):
        C = "четыре"
    if (unit == 5):
        C = "пять"
    if (unit == 6):
        C = "шесть"
    if (unit == 7):
        C = "семь"
    if (unit == 8):
        C = "восемь"
    if (unit == 9):
        C = "девять"
    return B,C

def determineHowMuchMore(a,b):#6
    if a > b:
        c = a - b
        ans = 'a больше чем b на '
    else:
        c = b - a
        ans = 'b больше чем a на'
    return ans, c

def difinetherange(a):#7
    if (a >= 0) and (a <= 10):
        ans = ('от 0 до 10')
    elif (a >= 20) and (a <= 30):
        ans = ('от 20 до 30')
    elif (a >= 40) and (a <= 50):
        ans = ('от 40 до 50')
    return ans

def checkTheAmount(a,b,c):#8
    if (a > b) and (a > c):
        summ = c + b
        maxx = a
    if (b > a) and (b > c):
        summ = a + c
        maxx = b
    if (c > a) and (c > b):
        summ = a + b
        maxx = c
    if summ > maxx:
        ans='Сумма меньших чисел больше большего'
    else:
        ans='Сумма меньших чисел меньше большего'
    return ans






