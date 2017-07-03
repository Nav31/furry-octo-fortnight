def high_and_low(numbers):
    numbers = numbers.split()
    intNumbers = []
    for number in numbers:
        intNumbers.append(int(number))
    intNumbers.sort()
    return "" + str(intNumbers[-1:][0]) + " " + str(intNumbers[0:1][0])

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))

# Best Answer
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))