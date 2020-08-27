# How many possible paths are there in a 20 X 20 grid from the top right to
# the bottom left, when only moving down and right?

# This is the grid problem in combinatorics, look it up for more info on problems like these
def factorial(n):
    L = list(range(1,n+1))
    v = 1
    for x in range(n):
        v = v * L[x]
    return v

def grid_paths(n):
    result = factorial(2*n)// (factorial(n) * factorial(n))
    return result

print(grid_paths(20))
