#What is the value of the first triangular number to have over five hundred divisors?
import time
start = time.time()

def tri_num(n):
    t = (n * (n+1))//2
    return t

def factor_len(n):
    L = [x for x in range(1,n+1) if n%x == 0]
    return len(L)

n = 1
a = int()
while a < 500:
    if n % 2 == 0:
        a = factor_len(n//2) * factor_len(n+1)
    else:
        a = factor_len(n) * factor_len((n+1)//2)
    n += 1

print(a, n-1, tri_num(n-1))

end = time.time()
print()
print(end - start)
