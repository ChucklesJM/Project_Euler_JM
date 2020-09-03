#Find the maximum path sum in the triangle below
import time
start = time.time()

def max_path(triangle):
    triangle = [int(x) for x in triangle.split()]
    n = int( (2 * len(triangle) + (0.25))**(1/2) - 0.5 + 1)
    tri = lambda n: (n * (n+1)) // 2
    X = list(map(tri, list(range(n-1))))
    Y = list(map(tri, list(range(1,n))))
    condense = lambda x,y : (x,y)
    rows = [triangle[a:b] for a,b in list(map(condense, X, Y))]
    while len(rows) > 1:
        for x in range(len(rows[-1])-1):
            if rows[-1][x] >= rows[-1][x+1]:
                rows[-2][x] += rows[-1][x]
            else:
                rows[-2][x] += rows[-1][x+1]
        del rows[-1]
    return rows

triangle = open("problem_67_triangle.txt",'r')
triangle = triangle.read()

print(max_path(triangle))

end = time.time()
print(end-start)

#Runtimes:
# 1. 0.003988504409790039
# 2. 0.002991914749145508
# 3. 0.004024982452392578
# 4. 0.003989219665527344
# 5. 0.0029921531677246094
