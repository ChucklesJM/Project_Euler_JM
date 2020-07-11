#Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

#Generating a list with natural numbers 1-100.
nums = list(range(101))
#print(nums)

#Find the square of the sum (1+...+100).

# The following is old code: (that does work.)
#LIST = nums
#x = 0
#total = 0
#while x < 101:
#    print('index: ', x)
#    print('total sum thus far: ', total)
#    hold = LIST[x]
#    total = total + hold
#    x += 1

#print('the sum of 1-100 is:', total)


LIST = list(range(101))

#Funtion for the trianuglar numbers:
def tri_num(n):
    n = int(n)
    sum = n * (n+1)
    sum = sum / 2
    sum = int(sum)
    return sum

a = tri_num(100)
print(a)
print(a*a)

#Function for the triangular numbers but every term is squared, (e.g. 1^2 + 2^2 + ...)
def tri_num_sqrd(n):
    n = int(n)
    sum = n * (n+1) * ((2*n)+1)
    sum = sum / 6
    sum = int(sum)
    return sum
b = tri_num_sqrd(100)
print(b)

print()
print("The answer to problem 6 is: ")
print((a*a) - b)
