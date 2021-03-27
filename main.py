# This is a sample Python script to practice the usage of the generators in Python.
# EXERCISE 1: Fibonacci numbers
def fibonacci1(number):
    count = 0
    num1, num2 = 0, 1
    while count < number:
        yield num1
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        count += 1


print("EXERCISE 1\nFibonacci numbers:")
fin = fibonacci1(10)
for i in fin:
    print(i)


def power_number(num):
    return num * num


def get_square1(num):
    for j in range(num):
        yield power_number(j)


def get_square2(num):
    for j in range(num):
        yield power_number(j)


print("\nEXERCISE 2\nPower Function:")
test1 = get_square1(11)
print("This is a list to return power function: ", (list(test1)))

test2 = get_square2(11)
print("This is a for loop to return power function:")
for i in test2:
    print(i)
