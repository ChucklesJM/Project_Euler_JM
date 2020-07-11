#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Not proud of this one chief, pretty inelegant. Totally brute forced this. Though in my defense it was 3 am when I coded this. 
x = 1
while x > 0:
    if not x % 1 == 0:
        x += 1
        continue

    if not x % 2 == 0:
        x+= 1
        continue

    if not x % 3 == 0:
        x += 1
        continue

    if not x % 4 == 0:
        x+= 1
        continue

    if not x % 5 == 0:
        x += 1
        continue

    if not x % 6 == 0:
        x+= 1
        continue

    if not x % 7 == 0:
        x += 1
        continue

    if not x % 8 == 0:
        x+= 1
        continue

    if not x % 9 == 0:
        x += 1
        continue

    if not x % 10 == 0:
        x+= 1
        continue

    if not x % 11 == 0:
        x += 1
        continue

    if not x % 12 == 0:
        x+= 1
        continue

    if not x % 13 == 0:
        x += 1
        continue

    if not x % 14 == 0:
        x+= 1
        continue

    if not x % 15 == 0:
        x += 1
        continue

    if not x % 16 == 0:
        x+= 1
        continue

    if not x % 17 == 0:
        x += 1
        continue

    if not x % 18 == 0:
        x+= 1
        continue

    if not x % 19 == 0:
        x += 1
        continue

    if not x % 20 == 0:
        x+= 1
        continue

    print(x)
    break
