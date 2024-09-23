from math import sqrt

print(5%3)

print(10%4)



def get_divisors(n):
    s = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return s

print(get_divisors(18))

def is_Prime(n):
    return (len(get_divisors(n)) == 2 )

print(is_Prime(7))
print(is_Prime(8))


# 최대공약수
def get_GCD(a,b):
    setA = get_divisors(a)
    setB = get_divisors(b)
    return max(setA & setB)

print(get_GCD(12,8))

# 최소공배수
def getLCM(a,b):
    return (a * b // get_GCD(a,b))

print(getLCM(12,8))

# 소인수분해
def getPrimes(n):
    primes = []
    for i in range(2,n+1):
        while n % i == 0:
            primes.append(i)
            n //= i
    return primes
        
print(getPrimes(60))

# 에라토스테네스의 체 알고리즘
N = 120
isPrime = [True] * (N + 1)
isPrime[1] = False
for i in range(2, int(sqrt(N)) +1):
    if not isPrime[i]:
        continue
    for j in range(2 * i, N + 1, i):
        isPrime[j] = False
        
        
print(isPrime)

# 유클리드 알고리즘
def gcd(a,b):
    if b == 0 :
        return a
    return gcd(b, a%b)

print(gcd(12,8))
