#Find the maximum total from top to bottom of the triangle below:
import math
import time
start = time.time()

L = [75,
95, 64,
17, 47, 82,
18, 35, 87, 10,
20, 4, 82, 47, 65,
19, 1, 23, 75, 3, 34,
88, 2, 77, 73, 7, 63, 67,
99, 65, 4, 28, 6, 16, 70, 92,
41, 41, 26, 56, 83, 40, 80, 70, 33,
41, 48, 72, 33, 47, 32, 37, 16, 94, 29,
53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,
70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,
91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,
63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,
4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

#number of rows in the triangle plus one

n = int(math.sqrt(2 * len(L) + (0.25)) - 0.5 + 1)
m = 0

indices = []

for x in range(1,n):
    hold = m
    m = m + x
    indices.append((hold, m))

rows = []

print(indices)

for x, y in indices:
     A = L[x:y]
     rows.append(A)

ID = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

list_path_sums = []

while not sum(ID) == 15:
    path_sum = rows[0][0]
    y = 0
    r = 1
    for x in range(14):

        if ID[x] == 0:
            path_sum += rows[r][y]
            r += 1

        else:
            y += 1
            path_sum += rows[r][y]
            r += 1

    list_path_sums.append(path_sum)

    ID[0] += 1

    for i in range(14):
        if ID[i] == 2:
            ID[i] = 0
            if i+1 == 14:
                ID[i] = 2
            else:
                ID[i+1] += 1

print(ID)
print(len(list_path_sums))
list_path_sums.sort()
print(list_path_sums[-1])
end = time.time()
print(end - start)
