
def function():
    function()


def sum_of_digits(number):
    sum = 0
    while number>0:

        d = number%10
        sum += d
        number = number//10
    return sum
print(sum_of_digits(666))

def factorial(number):
    product = 1
    for i in range(1,(number+1)):
        product *= i
    return product

print(factorial(5))

# using recursion function:
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))


def sod(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sod(number//10)
print(sod(666))


