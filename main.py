def calculates_palidroms(number):
    if len(str(number)) % 2 == 0:
        left_part = (number - number %  10 ** (len(str(number)) / 2)) / 10 ** (len(str(number)) / 2)
        right_part = number % 10 ** (len(str(number)) / 2)
    else:
        left_part = (number - number % 10 ** (len(str(number)) / 2 + 0.5)) / 10 ** (len(str(number)) / 2 + 0.5)
        right_part = number % 10 ** (len(str(number)) / 2 - 0.5)

    if int(right_part) == int(str(int(left_part))[::-1]):
        return True
    else:
        return False


for i in range(100000,1000000):
    firts_palindrom = i % 100000
    second_palindrom = (i + 1) % 100000
    third_palindrom = ((i+2) % 100000 - (i+2) % 10) / 10
    if calculates_palidroms(i+3) and calculates_palidroms(firts_palindrom) and calculates_palidroms(second_palindrom) \
            and calculates_palidroms(int(third_palindrom)):
        print(i)
