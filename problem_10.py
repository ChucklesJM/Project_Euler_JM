#Find the sum of all the primes below two million.

def primes_Lthan(n):
    #Making sure n is an integer
    n = int(n)
    #Generating a list of odd intergers to save time
    check = list(range(3, n + 1, 2))
    #As a result of the line above we gotta manually add 2 as a prime
    primes = [2]
    #x is going to be our index for the next part
    x = 0


    #Debug code:
    #print( )
    #print("range in question is 0 to ",check[-1])
    #print()
    #print("checking: ", check)
    #print()

    #The plan is to remove every prime once we've found it and every non-prime
    # from the list of values we're checking so eventually the list of values
    # we're checking will be empty
    while not check == []:

        #I guess we didn't need to set x above, since we'll need it back at 0
        # everytime we're done combing through the list for non-primes
        x = 0

        #p is least in the number to check
        p = check[0]
        #and p is also prime
        primes.append(p)
        #the part where we remove the prime once we've catalogued it
        del check[0]

        #while loop used to do the combing, once x == len(check) - 1 we've reached
        # the last element in the list and so the first element in the list will
        # be prime so we go back to beginning and catalogue it
        while x < len(check):

            if check[x] % p == 0:
                del check[x]

            x += 1

            #Debug code:
            #print(x)
        #print("primes found, ",len(primes))

    return primes

all = primes_Lthan(2000000)

#Debug code:
#print()
#print("last prime found: ", all[-1])
#print()
#print(all)
#print()

#Some set-up for the next part
total = 0
a = 0

#Recursive loop for adding things together, another way to do this would be to
# add the first value in all to total then delete it, that way you wouldn't have
# to code the increasing index
while a < len(all):

    total = all[a] + total
    a += 1

    #Debug code:
    #print(total)

print( )
print("the sum you're looking for is: ",total)
print( )

#Run this and go get lunch or something
