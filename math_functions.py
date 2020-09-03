#In order to import and use these functions you will need the following lines of code:
#For a specific function:
#       from math_functions import *function name*

#For all functions:
#       import math_functions
#Note: in order to use the functions in this case you will need to write:
#       math_functions.*function name*()
#________________________________________________________________
#________________________________________________________________
#Returns the sum of all the integers between l and L that are multiples
# of n and m.

def sum_ints(n,m,l,L):
    S = sum([x for x in range(l,L) if x%n==0 or x%m==0])
    return S

#_______________________________________________________________

#Making a function to reverse a number
def int_reverse():
    num = int(input("Enter an integer to reverse here: "))
    temp = num
    hold = 0
    rev = 0
    while temp > 0:
        hold = temp % 10
        rev = (rev * 10) + hold
        temp = temp - hold
        temp = temp / 10
        rev = int(rev)
        continue
    print("The reverse is: ", rev,)

# to cal the function above use : int_reverse()

def rev_num(num):
    temp = num
    hold = 0
    rev = 0
    while temp > 0:
        hold = temp % 10
        rev = (rev * 10) + hold
        temp = temp - hold
        temp = temp / 10
        rev = int(rev)
    return rev
    #print("Input (num): ", num)
    #print("Output (rev): ", rev)

# to call this function use : rev_num(12345) e.g.
#______________________________________________________________


#Funtion for the trianuglar numbers:
def tri_num(n):
    n = int(n)
    sum = n * (n+1)
    sum = sum / 2
    sum = int(sum)
    return sum

#Function for the triangular numbers but every term is squared, (e.g. 1^2 + 2^2 + ...)
def tri_num_sqrd(n):
    n = int(n)
    sum = n * (n+1) * ((2*n)+1)
    sum = sum / 6
    sum = int(sum)
    return sum

#_______________________________________________________________

#Function for checking if a number is prime:

def check_prime(n):
    n = int(n)
    num_prime = True
    if n % 2 == 0:
        num_prime = False
        return num_prime

    for x in range(3, n-1):
        if n % x == 0:
            num_prime = False
            break
        else:
            return num_prime
    return num_prime
#______________________________________________________________

#Function for seperating a positive integer into a list of its digits:

def make_digits(n):
    digits = []
    n = int(n)
    temp = n
    while temp > 0:
        hold = temp % 10
        digits.append(hold)
        temp = temp - hold
        temp = temp // 10
    digits.reverse()
    return digits
#______________________________________________________________

#Function for making a list of factors:

def factors(n):
    factors = []
    n = int(n)
    for x in range(1,n+1):
        if n%x == 0:
            factors.append(x)
    return factors

#Alternatively

def fact(n):
    return sum([x for x in range(1,n) if n%x == 0])

#Function for checking if two integers are relatively prime:
#(requires the one above to work)

def rel_prime(m,n):
    m = int(m)
    n = int(n)

    if n > m:
        t = m
        m = n
        n = t

    m_facts = factors(m)
    n_facts = factors(n)

    check = []
    y = 0
    x = len(n_facts) - 1

    while len(n_facts) > 0:

        if not n_facts[x] == m_facts[y]:
            y += 1
        else:
            check.append(n_facts[x])
            y += 1

        if y == len(m_facts) - 1:
            y = 0
            del n_facts[x]
            x -= 1

        if x == -1:
            break

    rel = True

    if not check == [1]:
        rel = False
    return rel

#Function for finding a pythagorean triple based off of Euclid's function
# to call the triple write
        #Euclid_form(m,n)[0]
# to check whether its a primitive triple write
        #Euclid_form(m,n)[1]

#what you're doing is calling an entry from a tuple created by the function
# you can also save the tuple under a different name by writing
        #new_name = Euclid_form(m,n)

def Euclid_form(m,n):
    m = int(m)
    n = int(n)

    if n > m:
        t = m
        m = n
        n = t

    prim = True

    if m%2 == 0 and n%2 == 0:
        prim = False

    if not m%2 == 0 and not n%2 == 0:
        prim = False

    if not rel_prime(m,n):
        prim = False

    a = m**2 - n**2
    b = 2*n*m
    c = m**2 + n**2

    triple = [a,b,c]

    return triple, prim

#____________________________________________________________

#Function for finding all the primes less that a given integer
# this is slow though

def primes_Lthan(n):
    n = int(n)
    check = list(range(2, n + 1))
    primes = []
    x = 0

    while not check == []:

        x = 0
        p = check[0]
        primes.append(p)
        del check[0]

        while x < len(check):

            if check[x] % p == 0:
                del check[x]

            x += 1

    return primes

#This is a better version based off of the pseudo code on the wiki page

def Sieve_Erato(n):
    primes = []
    check = [True for n in range(0, n+1)]
    for i in range(2, n+1):
        if check[i] == True:
            primes.append(i)
            for j in range((i)**2,n+1,(i)):
                try: check[j] = False
                except: pass
    return primes

#___________________________________________________________

#Function will find the largest product of adjascent numbers in any direction
# in the array. The two arguments of the function are an array and the # of numbers
# in the product.
#A is the array
#p is the # of numbers in the product

def adj_prod(A, p):

    a = len(A)
    b = len(A[0])

    P = p - 1

    h = []
    for i in range(a):
        for j in range(b-P):
            l = A[i][j]
            for x in range(1, p):
                l = l * A[i][j + x]
            h.append(l)
    h.sort()

    v = []
    for i in range(a-P):
        for j in range(b):
            l = A[i][j]
            for x in range(1, p):
                l = l * A[i + x][j]
            v.append(l)
    v.sort()

    df = []
    for i in range(a-P):
        for j in range(b-P):
            l = A[i][j]
            for x in range(1, p):
                l = l * A[i + x][j + x]
            df.append(l)
    df.sort()

    db = []
    for i in range(a-P):
        for j in range(P,b):
            l = A[i][j]
            for x in range(1,p):
                l = l * A[i + x][j - x]
            db.append(l)
    db.sort()

    L = [h[-1], v[-1], df[-1], db[-1]]
    L.sort()
    return L[-1]

#_________________________________________________________________
#Function for finding the factorial of an interger n.

def factorial_old(n):
    L = list(range(1,n+1))
    v = 1
    for x in range(n):
        v = v * L[x]
    return v

#Here is a more elegant function for finding the factorial of n:

def factorial(n):
    F = math.prod(list(range(1,n+1)))
    return F

#Function for finding the sum of the digits of a factorial of an integer n.
# requires the functions factorial(n) and make_digits(n) to work properly.

def sum_fact_digits(n):
    S = sum(make_digits(factorial(n)))
    return S

#Here is a function that adds the digits of the factorial of n,
# better than the above:

def Fact_sum_dig(n):
    F = str(math.prod(list(range(1,n+1))))
    S = 0
    for x in range(len(F)):
        S = int(F[x]) + S
    return S

#________________________________________________________________
#Functtion finds the longest collatz sequence in the range 0 to a,
# returns the number and the length of the sequence associated to it

def Collatz_length(a):
    dict = {1 : 0}

    for n in range(1,a+1):
        L = [1]
        v = n
        while v > 1:
            L.append(v)
            if v % 2 == 0:
                v = v//2
            else:
                v = 3 * v + 1
        dict[n] = len(L)
    result = []
    a = 0
    for x in dict:
        if dict[x] > a:
            a = dict[x]

    for x, y in dict.items():
        if y == a:
            result.append((x, y))
    return result

#_________________________________________________________________
#Function finds the maximum path sum in a triangle starting from
# the top moving to the bottom

def max_path(triangle):
    triangle = [int(x) for x in triangle.split()]
    n = int( (2 * len(triangle) + (0.25))**(1/2) - 0.5 + 1)
    tri = lambda n: (n * (n+1)) // 2
    X = list(map(tri, list(range(n-1))))
    Y = list(map(tri, list(range(1,n))))
    condense = lambda x,y : (x,y)
    rows = [triangle[a:b] for a,b in list(map(condense, X, Y))]
    while len(rows) > 1:
        for x in range(len(rows[-1])-1):
            if rows[-1][x] >= rows[-1][x+1]:
                rows[-2][x] += rows[-1][x]
            else:
                rows[-2][x] += rows[-1][x+1]
        del rows[-1]
    return rows
