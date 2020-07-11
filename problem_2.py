# Find the sum of all even Fibonacci numbers whose value does not exceed four million
#defining relevant lists
Fib = [1,2]
Even_Fib = []
x = 0

#generating the necessary fib numbers
while Fib[-1] < 4000000:
    a = Fib[x] + Fib[x+1]
    x += 1
    Fib.append(a)

#checking to see if gottem
print(Fib)

#pulling out all even fib numbers into list
for a in Fib:
    if a%2 == 0:
        Even_Fib.append(a)

#check last step and summing
print(Even_Fib)
print("...and the answer is:", sum(Even_Fib))
