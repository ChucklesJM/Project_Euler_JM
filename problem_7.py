#what is the 10001st prime number?

#set-up
primes = []
p = 2

#Setting up the loop
while not len(primes) == 10001:
    num_prime = True

#Eleminate any even candidate primes
    if p > 3 and p % 2 == 0:
        p += 1
        continue

#Check if the candidate is divisible by any odd numbers
    for x in range(3, p-1, 2):
        if p % x == 0:
            num_prime = False
            break

    #print("Checked :", p)

#Processing the result of the check above
    if num_prime == False:
        p += 1
        continue

    if num_prime == True:
        primes.append(p)
        #print("%d is prime" %p)
        p += 1

    #print("Number of primes found: ",len(primes))

#Reporting the last known prime
primes.sort()
#print(primes)
print("last prime found was %d" %primes[-1])
print("the number of primes found was %d" %len(primes))

# first full run clocked in at: 10:17.64 (min:sec)
# second run: 9:29.96
# third run: 6:14.07
# fourth run: 2:36.36
# fifth run: 2:33.37  
# sixth run: 00:29.76 ***current state***
