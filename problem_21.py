#If the sum of all factors of a = b and if the sum of all factors of b = a
# then a and b are amicable numbers.
#Find the sum of all amicable numbers under 10000.



def sum_fact(n):
    return sum([x for x in range(1,n) if n%x == 0])

nums = []

check = list(range(10001))

for x in check:
    a = sum_fact(x)
    if x == sum_fact(a):
        nums.append(a)
        nums.append(x)
        check.remove(a)

print(sum(nums))
