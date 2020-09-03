#Solution to project euler #18: find the maximum path sum from the top to the bottom of the given triangle

#Timing
import time
start = time.time()

#Defining the function for reuseability
def max_path(triangle):
    #What we're looking to do is make a set for each row of the triangle we inputted
    #Splitting up the triangle which needs to be inputted as a string
    triangle = [int(x) for x in triangle.split()]
    #Using the triangular number equation to give the number of rows the triangle has
    n = int( (2 * len(triangle) + (0.25))**(1/2) - 0.5 + 1)
    #tri is defined to be the triangular number equation
    tri = lambda n: (n * (n+1)) // 2
    #We notice that the index beginning each row in the list is a triangular number
    # and the the index at the end of each row in the list is also a triangular number
    # so we generate a list of trangular numbers starting at 0 going to tri(n-1)
    # and a list starting at 1 going to tri(n), these are X and Y respectively
    X = list(map(tri, list(range(n-1))))
    Y = list(map(tri, list(range(1,n))))
    #New function condense, that takes two lists and makes a list of ordered pairs
    condense = lambda x,y : (x,y)
    #Generates the list of rows using the condense function on X and Y
    rows = [triangle[a:b] for a,b in list(map(condense, X, Y))]
    #For this next part we will be deleting every row once we are done with it
    # which gives us the logical condition of while rows has more than one element
    # because to get the largest path sum we will be adding the largest "child" to
    # the "parent" above it
    #If you're interested in how this works un-note the print statment in the loop
    while len(rows) > 1:
        #print(rows)
        for x in range(len(rows[-1])-1):
            if rows[-1][x] >= rows[-1][x+1]:
                rows[-2][x] += rows[-1][x]
            else:
                rows[-2][x] += rows[-1][x+1]
        del rows[-1]
    #The function returns the result of the while loop above
    return rows

#Triangle is save here as a multi-line string using """ """.
triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

#Answer
print(max_path(triangle))

#Timing
end = time.time()
print(end-start)
