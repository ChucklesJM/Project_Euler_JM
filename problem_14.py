#Which starting number, under one million, produces the longest chain?
#i.e. Find the Collatz sequence with a strating number that is less than 1 million that has the
# largest resulting chain.

import time
start = time.time()


def Collatz_length(a):

    #Builds a dictionary of numbers and their associated collatz length
    dict = {1 : 1}

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

    #Looks for the largest collatz length as a value in the dictionary
    result = []
    a = 0
    for x in dict:
        if dict[x] > a:
            a = dict[x]

    #Finds the key associated with the largest value and returns both
    # or any list of numbers that have equally long collatz lengths
    for x, y in dict.items():
        if y == a:
            result.append((x, y))
    return result

print(Collatz_length(1000000))


end = time.time()
print(end - start)
