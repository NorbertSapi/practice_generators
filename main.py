# This is a sample Python script to practice the usage of the generators in Python.
# EXERCISE 1: Fibonacci numbers

# fibonacci method
def fibonacci1(number):
    count = 0
    num1, num2 = 0, 1
    while count < number:
        yield num1
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        count += 1


# call the fibonacci method
print("EXERCISE 1\nFibonacci numbers:")
fin = fibonacci1(10)
for i1 in fin:
    print(i1)


# Exercise 2: Power Function
# this is the power function
def power_number(num):
    return num * num


def get_square1(num):
    for i2 in range(num):
        yield power_number(i2)


def get_square2(num):
    for j2 in range(num):
        yield power_number(j2)


print("\nEXERCISE 2\nPower Function:")
test1 = get_square1(11)
print("This is a list to return power function: ", (list(test1)))

test2 = get_square2(11)
print("This is a for loop to return power function:")
for i in test2:
    print(i)

# Exercise 3: print even numbers and odd numbers.
print("EXERCISE 3\nEven Numbers from a list:")


# method to return even numbers
def even_numbers(num):
    for i3 in range(num):
        if i3 % 2 == 0:
            yield i3


# method to return odd numbers
def odd_numbers(num):
    for j3 in range(num):
        if j3 % 2 != 0:
            yield j3


# print even numbers using list()
print(list(even_numbers(20)))
# print odd numbers using 'for loop'
print("Odd Numbers from a for loop:")
test_odd = odd_numbers(20)
for j in test_odd:
    print(j)
