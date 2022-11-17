import math


def ean_validation(ean):

    multiplication_sum = 0

    for number in range(0, 12):

        if number % 2 == 0:
            multiplication_sum += int(ean[number]) * 1
        else:
            multiplication_sum += int(ean[number]) * 3

    digit = ((((math.floor(multiplication_sum/10)) + 1) * 10) - multiplication_sum)
    if digit % 10 == 0:
        digit = 0

    currect = f"{ean[0:12]}{digit}"

    return currect
