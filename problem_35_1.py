#Find how many circular primes are there below one million.

import time
S = time.time()

def primesL_than(n):
    primes = []
    check = [True for n in range(0, n+1)]
    for i in range(2, n+1):
        if check[i] == True:
            primes.append(str(i))
            for j in range((i)**2,n+1,(i)):
                try: check[j] = False
                except: pass
    return primes

primes = [str(x) for x in primesL_than(100)]
for prime in primes:
    for x in ["0","2","4","5","6","8"]:
        if x in prime:
            primes.remove(prime)
print(primes)

circular_primes = []

for prime in primes:

    rotations = []

    for index in prime:
        rotations.append(prime)
        prime = prime[-1] + prime[:-1]

    circular = True

    for number in rotations:
        if not number in primes:
            circular = False

    if circular == True:

        for number in rotations:
            if int(number) in circular_primes:
                pass
            else:
                circular_primes.append(int(number))

print(len(circular_primes))

E = time.time()
print(E-S)
