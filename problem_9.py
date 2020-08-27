#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc, where a < b < c.
from math_functions import factors
from math_functions import rel_prime
from math_functions import Euclid_form
#Write an application of Fibonacci Method:

m = 2
n = 1

while n > 0:
    tri = Euclid_form(m,n)[0]
    a = tri[0]
    b = tri[1]
    c = tri[2]

    if a + b + c == 1000:
        print(tri)
        print(a*b*c)
        break

    m += 1

    if a + b + c > 1000:
        n += 1
        m = n + 1

# gonna include some other cool ways to solve this here:
# by user: Pier
    #Without programming:

    #a= 2mn; b= m^2 -n^2; c= m^2 + n^2;
    #a + b + c = 1000;

    #2mn + (m^2 -n^2) + (m^2 + n^2) = 1000;
    #2mn + 2m^2 = 1000;
    #2m(m+n) = 1000;
    #m(m+n) = 500;

    #m>n;

    #m= 20; n= 5;

    #a= 200; b= 375; c= 425;
#-----------------------------------
# by user: naimad
#I just wrote a silly little program on my calculator which finds (tries to ?)
# all the pythagorean triplets in a given range for 'a' and then ran it
# in range [3, 500]. I multiplied the first triplet whose sum was a
# divisor of 1000 so that its sum became 1000. This worked pretty good, because
# there soon was a triplet to be a divisor of 1000, namely (8, 15, 17), which was
# the fifth one. Its sum is 40, 1000 divided by 40 is 25, 25*(8, 15, 17)
# is (200, 375, 425).
