import sympy
import random

# range of seed and primes:
x = 3*10**10
y = 4*10**10

# seed - x
seed = random.choice(range(x, y))

# finds next prime
def prime_3modulo(x):
    n = sympy.nextprime(x)
    while(n % 4 != 3):
        n = sympy.nextprime(n)
    return n

# calculate x(i+1)
def moduloN(xn, N):
    return (xn**2) % N

def generate_bits(n):
    x1 = moduloN(seed, N)
    nb = bin(x1)[-1]
    for i in range(n-1):
        x1 = moduloN(x1, N)
        nb += bin(x1)[-1]
    return nb

# TESTY:
def count_ones(nb):
    count1 = 0
    count0 = 0
    for i in nb:
        if i == '0':
            count0 += 1
        else:
            count1 += 1
    count = {0: count0, 1: count1}
    return count

def count_series(nb):
    series = []
    count = 0
    for i in nb:
        if i == "1":
            count += 1
        else:
            if count > 0:
                series.append(count)
                count = 0
    seria = {i + 1: 0 for i in range(6)}

    for i in series:
        if i == 1:
            seria[1] += 1
        elif i == 2:
            seria[2] += 1
        elif i == 3:
            seria[3] += 1
        elif i == 4:
            seria[4] += 1
        elif i == 5:
            seria[5] += 1
        else:
            seria[6] += 1

    return seria

def long_series_test(nb):
    count = 0
    for i in nb:
        if i == "1":
            count += 1
        else:
            if count > 25:
                return False
            else:
                count = 0
    return True

def poker_test(nb):
    segments = []

    # dzielimy na segmenty:
    for i in range(0, len(nb), 4):
        segment = nb[i:i + 4]
        segments.append(segment)

    # zliczenie wystapien:
    count = {bin(i)[2:].zfill(4) : 0 for i in range(16)}
    for i in segments:
        count[i] += 1

    # zliczenie X:
    summ = 0
    for i in count:
        summ += count[i]**2
    x = 16/5000 * summ - 5000

    return x


# RESULTS OF TESTS:
def test1():
    print("TEST 1.")
    count = count_ones(nb)
    print(count)

def test2():
    print()
    print("TEST 2.")
    count = count_series(nb)
    for i in count:
        print(i, ":", count[i])

def test3():
    print()
    print("TEST 3.")
    if(long_series_test(nb)):
        print("Test długiej serii - PASSED")
    else:
        print("Test długiej serii - FAILED")

def test4():
    print()
    print("TEST 4.")
    x = poker_test(nb)
    print("X wynosi:", x)

# next prime after x
p = prime_3modulo(x)
# next prime after y
q = prime_3modulo(y)

N = p*q

nb = generate_bits(20000)

# TEST 1.
test1()

# TEST 2.
test2()

# TEST 3.
test3()

# TEST 4.
test4()
