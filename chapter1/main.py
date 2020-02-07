def checkparity(number):
    count = 0
    while number > 0:
        if number & 1 == 1:
            count += 1
        number = number >> 1
    return count % 2 == 0

print(not checkparity(11))
