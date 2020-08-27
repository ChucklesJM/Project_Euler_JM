#What is the sum of the digits of the number 2^1000?

def make_digits(n):
    digits = []
    n = int(n)
    temp = n
    while temp > 0:
        hold = temp % 10
        digits.append(hold)
        temp = temp - hold
        temp = temp // 10
    digits.reverse()
    return digits

print(sum(make_digits(2**(1000))))
