def zeros(n):
    count = 0  # initialize return value
    i = 5  # to get result without calculating factorial we only have to count all fives in presented number
    while (n / i >= 1):  # we divide input number to 5
        count += int(n / i)  # after division, we count all occurences of 5 without last one
        i *= 5  # last one if number itself / 5*5
    return int(count)


print(zeros(6))
