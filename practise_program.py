"""
write a Python program to swap first and last element of the list.
Examples:
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]
Input : [1, 2, 3]
Output : [3, 2, 1]
"""

print("Python program to swap first and last element of the list")
list = [12, 35, 9, 56, 24]
print(list)

# len(list)-1
# list[0],list[-1] = list[4],list[0]
# print(list)
# print("**************************************")

# print("Swapping the number using function")
# print(list)
# def swaping_the_numbers(list):
#     temp = list[0]
#     list[0] = list[-1]
#     list[-1] = temp
#     return list
# print(swaping_the_numbers(list))

# print("*****************************************")
# def swaplist(list):
#     first = list.pop(0)
#     last = list.pop(-1)
#
#     list.insert(0, last)
#     list.append(first)
#     return list
# print(swaplist(list))

#_____________________________________________________________________
#Add Two Numbers
# print("#######################################")
# print("Adding two numbers")
# num1 = 45
# num2 = 85
# print("sum:",num1 + num2)

# print("***************************")

# a = int(input("Enter First number:"))
# b = int(input("Enter the Second number: "))
# sum = a + b
# print(sum)
# print("sum of a and b is:",sum)

# print("******************************")
#
# def add(a,b):
#     return a + b
#
# print(add(5,4))
# #_____________________________________________________________________-

#Find the Square Root
print("#########################################")
print("Find the Square root of the number")


#______________________________________________________________________
#Calculate the Area of a Triangle
# print("#################################")
# print("calculate the Area of Triangle")
# base = 5
# height = 4
#
# mult = base * height
# area_of_triangle = 1/2 * mult
# print(int(area_of_triangle))
#
# print("****************************************")
# print("Calculating the area of triangle using function")
#
# def area_of_triangle(base,height):
#     return 1/2 * base * height
#
# base = float(input("Enter the value of base:"))
# height = float(input("Enter the value of height: "))
#
# print(area_of_triangle(base,height))


#_______________________________________________________________________
# L = ['a', 'b', 'c', 'd']
# res = ''.join(L)
# print(res)
#
# for i in range(10, 15, 1):      #range(start,stop,step)
#     print(i, end=',')
#
# for i in range(1, 5):          #range(start,stop)
#     print(i)
# else:
#     print("this is else block statement")

print("###############################################")
print("Maximum of two numbers in Python")

# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
#
# if num1 > num2:
#     print("Maximum number is:", num1)
# else:
#     print("Maximum number is:", num2)

print("********************************************")

# def maximum(a,b):
#     return a < b
# print(maximum(4,1))

print("***************************************")

# def maximum1(a,b):
#     if a >= b:
#         return a
#     else:
#         return b
# print(maximum1(5,4))

# def maximum1(a,b):
#     if a >= b:
#         return a
#     else:
#         return b
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
#
# print(maximum1(a,b))



# print("Python Program for factorial of a number")



# print("Python Program for simple interest")
# # SI = P*T*R/100
# def simple_intereset(p,t,r):
#     print("Principal is:",p)
#     print("Time is:",t)
#     print("Rate is:",r)
#
#     return p*t*r/100
#
# print(simple_intereset(5,4,8))




# print("Python Program for compound interest")
# A = P(1 + R/100)t(power of t)
# Compound Interest = A – P

# def compound_interest(principal, rate, time):
#     Amount = principal * (pow((1 + rate / 100), time))
#     CI = Amount - principal
#     print("Compound interest is", CI)
#
# principal = int(input("Enter the principal amount: "))
# rate = int(input("Enter rate of interest: "))
# time = int(input("Enter time in years: "))

# compound_interest(principal, rate, time)
#
#
# print("Python program to print all Prime numbers in an Interval")


# i = 1
# j = 1
# while j<11:
#     while i<11:
#         print(f"{j}*{i}={i * j}")
#         i +=1
#     print("_______")
#     j +=1


# program to find sum of multiple numbers

# def find_sum(*numbers):
#     result = 0
#
#     for num in numbers:
#         result = result + num
#
#     print("Sum = ", result)


# function call with 3 arguments
# find_sum(1, 2, 3)

# function call with 2 arguments
# find_sum(4, 9)
#
# def greet(*msg):
#     for m in msg:
#         print(m)
#
# greet("hello","to","all")

# *args parameters:

# def funargs(*args):
#     print(args[0])
# har = ["abc","def","ghi","jkl"]
# funargs(*har)
#
# def fun1(*har):
#     print(type(har))
#     print(har[0])
# fun1("abcd","efgh","ijkl")


# Calculator program in python

# def calculator(a,b):
#     result = 0
#     a + b
#     return result
#
#
# calculator(5,2)
#
#
# print("Iterate through a python string")
# greet = 'Hello'
# # iterating through greet string
# for letter in greet:
#     print(letter)
#

# print("String Membership Test")
# print('a' in 'program')
# print('at' not in 'battle')
#
#
# print("Escape Sequences in Python")
#
# print("while loop in python")
# count = 0
# while (count < 3):
#     count = count + 1
#     print("Hello PrepBuddy")
#
# print("Here is the for loop example with List, Tuple, string, and dictionary iteration using For Loops")
# print("List Iteration")
# l = ["For", "Learning", "Coding,", "join", "PrepBytes"]
# for i in l:
#     print(i, end=" ")
#
# print("\nTuple Iteration")
# t = ("For", "Learning", "Coding,", "join", "PrepBytes")
# for i in t:
#     print(i, end=" ")

# print("\nString Iteration")
# s = "For Learning Coding Join PrepBytes"
# for i in s:
#     print(i, end ="")
#
# print("\nDictionary Iteration")
# d = dict()
# d['Prep'] = 123
# d['Bytes'] = 345
# for i in d:
#     print("%s %d" % (i, d[i]))
#
# print("\nSet Iteration")
# set1 = {1, 2, 3, 4, 5, 6}
#
# for i in set1:
#     print(i, end = " ")
#
#
# print("Python Nested if Statement")
# number = 5

# outer if statement
# if (number >= 0):
#
#  *   # inner if statement
#     if number == 0:
#         print('Number is 0')
#
#     # inner else statement
#     else:
#         print('Number is positive')
#
# # outer else statement
# else:
#     print('Number is negative')
#
# # Output: Number is positive
#
#
# print("Mini Calculator")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
#
# choice = ("press 1 for addition \n press 2 for substraction \n press 3 for multiplication \n press 4 for division")
# /
# if+7
# def pattern2(n):
#     for i in range(n,0,-1):
#         for _ in range(i):
#             print("*", end = " ")
#         print()
#
#
# pattern2(5)

# def pattern3(n):
#     for i in range(n):
#         for j in range(n):
#             print(end=" ")
#
#         for k in range(i + 1):
#             print("*", end=" ")
#         print()
#         n -= 1
# pattern3(5)


def pattern4(n):
    for i in range(n,0,-1):
        for k in range(0, n-i):
            print(end=" ")
        for j in range(i):
            print("*", end=" ")
        print()


pattern4(5)







