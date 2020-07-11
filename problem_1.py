# Find the sum of all multiples of 5 and 3 below 1000
sum_list=[]

#Add all the numbers divisible by 3 and 5 to the sum list
for x in range(1000):
    if x%5==0:
        sum_list.append(x)
for x in range(1000):
    if x%3==0 and not x%5==0:
        sum_list.append(x)

print(sum_list)
#Add all the numbers in the sum list
print(sum(sum_list))
