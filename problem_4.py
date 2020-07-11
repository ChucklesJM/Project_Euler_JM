#Find the largest palindrome made from the product of two 3-digit numbers

#Hopefully importing the relevant function from reversing_funtions.py
#That didn't work, so I just copied the function over and added the return at the end

def rev_num(number):
    temp = number
    hold = 0
    rev = 0
    while temp > 0:
        hold = temp % 10
        rev = (rev * 10) + hold
        temp = temp - hold
        temp = temp / 10
        rev = int(rev)
    return rev

pallies = []
x = 100
y = 100

while x < 999 and y < 999 :

    #Makes sure that p is an integer, calculates the reverse of p, and adds one to x
    p = int
    p = x * y
    q = rev_num(p)
    x += 1

    #If the number p is equal to its reverse it is a pallindrome and goes into
    # the list of pallindromes
    if p == q:
        pallies.append(p)

        #Use this code if you want to see the x and y that results in each pallindrome
        # as it is calculated
        #print("||X is: ", x-1," ||Y is: ", y,  " ||Pallindrome: ", p)

    #Once the values of x (100-999) are exhausted, add one to y and start again
    if x == 999:
        x = 100
        y += 1

    #Probably useless code, but it makes me feel better
    if y == 999 and x == 999:
        break

#Rearrage the list of pallindromes to be ascending
pallies.sort()

#Gives the last pallindrome, which is the one the problem calls for
print("The number you seek is: ", pallies[-1])
print("The total number of pallindromes is: ", len(pallies))
