#two numbers are positive
def positive_numbers(a, b, c):
    positive = 0

    if a > 0:
        positive += 1
    if b > 0:
        positive += 1
    if c > 0:
        positive += 1

    return positive == 2

# testing data
print(positive_numbers(2, -4, -3))

