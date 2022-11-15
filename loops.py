
#1
def raiseToDegree(a,b):
    s = 1
    for i in range(b):
        s = s * a
    return s

def printNumbersthatAreMultipliesOfA(a):#2
    ans = []
    for i in range(1, 1001):
        if i % a == 0: ans += [i]
    return ans

def findTheNumbersWhoseSquareIsLessThanA(a):#3
    k = 0
    for i in range(1, a):
        if i**2<a: k += 1
    return k

def outputLargestDivisor(a):#4
    for i in range(a - 1, 1, -1):
        if a % i == 0: return i; break

def outputTheSumOfNumbersDivisibleBy7InAToB(a,b):#5
    summ = []
    for i in range(a, b + 1):
        if i % 7 == 0: summ += [i]
    return summ

def outputTheNumberOfTheFibonacciSeries(n):#6
    a = 1
    b = 1
    c = 1
    for i in range(n - 2):
        c = a + b;
        a = b;
        b = c
    return c

def findTheLargestDevisor(a,b):#7
    while a != b:
        if a > b:
            a = a - b
        else:
            b =b - a
    return a

def fintNUsingHalfDevision(z):#8
    a = 0
    b = z
    n = (a + b) / 2
    while n ** 3 != z:
        n = (a + b) / 2
        if n ** 3 > z:
            a = a
            b = n
        else:
            a = n
            b = b
    return int(n)

def countNumbersOfOddDigits(a):
    n = 0
    while a != 0:
        if a % 10 % 2 == 1: n += 1
        a //= 10
    return n

def mirrorTheNumber(a):#10
    z = 0
    while a != 0:
        z = z * 10 + a % 10
        a //= 10
    return z

def printTheNumbersInTheRange(a,b):#11
    for i in range(a, b + 1):
        chet = 0;
        nech = 0;
        num = i
        while num != 0:
            if num % 10 % 2 == 1:
                nech += num % 10
            else:
                chet += num % 10
            num //= 10
        if chet > nech: ans += [i]
    return ans

def areThereAnyIdenticalNumbers(a,b):#12
    k = False
    for i in range(len(a)):
        if a[i] in b:
            return 'ДА'
            k = True
            break
    if not k:
        return 'НЕТ'




