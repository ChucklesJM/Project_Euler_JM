#What is the largest prime factor of 600851475143?
#Set up some initial values
a = 2
b = 600851475143

#Get a loop set up so that we can have a recursive formula check for prime factors
while a > 0:

#If a is a prime factor list it and change b
    if b%a == 0:
        b = b/a
        print("factor:", a)
#If a is not a prime factor move onto the next interger
    else:
        a += 1

#Stop the script from running indefinitely
    if a > 1000000:
        break
