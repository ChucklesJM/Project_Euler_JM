#Find the sum of the digits in the number 100!

def factorial(n):
    L = list(range(1,n))
    v = 1
    for x in range(n-1):
        v = v * L[x]
    return v

def make_digits(n):
    digits = []
    temp = n
    while temp > 0:
        hold = temp % 10
        digits.append(hold)
        temp = temp - hold
        temp = temp // 10
    digits.reverse()
    return digits

def sum_fact_digits(n):
    S = sum(make_digits(factorial(n)))
    return S

print(sum_fact_digits(100))


#Also

import time
import math

start = time.time()

def F(n):
    F = str(math.prod(list(range(1,n+1))))
    S = 0
    for x in range(len(F)):
        S = int(F[x]) + S
    return S
print(F(100))

end = time.time()
print(end-start)

#Some noteworthy solutions found in the project euler thread on problem 20:

# by Begoner in Python:
# reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])

# by patrik_mrx in Python:

#def f(num):
#    result = 1
#    for i in range(1,num+1):
#        result *= i
#    return result
#
#
#number = f(100)
#sum = 0
#for i in str(number):
#    sum += int(i)
#print sum
