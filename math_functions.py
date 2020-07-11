#In order to import and use these functions you will need the following lines of code:
#For a specific function:
#       from math_functions import *function name*

#For all functions:
#       import math_functions
#Note: in order to use the functions in this case you will need to write:
#       math_functions.*function name*()
#______________________________________________________________________
#______________________________________________________________________

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
            return num_prime
        else:
            return num_prime
