"""
Types of operators:
1) Arithmetic Operators
2) Comparison Operators or Relational operators
3) Logical Operators
4) Bitwise Operators
5) Assignment Operators
6) Membership Operators
7)Identity Operators
8)Ternary operators

"""
# 1)Arithmetic operators:
# we can use + with string,list,tuple where both operands should be of same type.
# for * one operand should be string,list and one should be int.
num1 = 10
num2 = 2
str1 = "Hello"
str2 = " Developers"
lst1 = [5, 7, 50]
lst2 = [7, 69, 78]
lst3 = ["mango","grapes","bananas"]
tup1 =(4,8,6)
tup2 = (4,9,7)

print("Addition of two numbers:",num1 + num2, str1 + str2, lst1 + lst2, tup1 + tup2)
print("Subtraction of two numbers:", num1 - num2)
print("Multiplication of two numbers:",num1 * num2, num2 * str1, num2 * lst3)
print("Division Operator:",num1 / num2)
print("Modulo operator:",num1 % num2)
print("floor Division operator:",num1 // num2)
print("Exponent operator or power operator",num1 ** num2)

#Relational Operators: Can use for int,float,string,list,tuple ans sets.
# for list and tuple, 1st element is checked if they are unequal,return False,
# if equals we go for next element, until comparison results to False or
# the length of shorter list
# For sets comparison is done on basic of superset and subset
# < is subset
# > is superset
# we can have chaining of comparisons too, but if any comparison returns false
# the whole result will be false.

a = 23
b = 28
c = 17.2
d = 2.5

print("INTEGER")
print("Less than operator for int:",a < b)
print("Greather than operator for int:",a > b)
print("Less than equal to operator for int:",a <= b)
print("Greather than equal to operator for int:",a >= b)
print("Equal to equal operator:",a == b)
print("Not equal to operator:",a != b)

print("FLOAT")
print("Less than operator for float:",c < d)
print("Greather than operator for float:",c > d)
print("Less than equal to operator for float:",c <= d)
print("Greather than equal to operator for float:",c >= d)
print("Equal to equal operator for float:",c == d)
print("Not equal to operator for float:",c != d)

print("STRING")
str = "green"
str1 = "apple"
print("Less than operator for string:",str < str1)
print("Greather than operator for string:",str > str1)
print("Less than equal to operator for string:",str <= str1)
print("Greather than equal to operator for string:",str >= str1)
print("Equal to equal operator for string:",str == str1)
print("Not equal to operator for string:",str != str1)

print("LIST")
list1 = [1,2,3,4]
list2 = [5,6,7,8]
print("Less than operator for List:",list1 < list2)
print("Greather than operator for List:",list1 > list2)
print("Less than equal to operator for List:",list1 <= list2)
print("Greather than equal to operator for List:",list1 >= list2)
print("Equal to equal operator for List:",list1 == list2)
print("Not equal to operator for List:",list1 != list2)

print("TUPLE")
tuple1 = (1,8,4)
tuple2 = (7,6,1)
print("Less than operator for Tuple:",tuple1 < tuple2)
print("Greather than operator for Tuple:",tuple1 > tuple2)
print("Less than equal to operator for Tuple:",tuple1 <=tuple2)
print("Greather than equal to operator for Tuple:",tuple1 >=tuple2)
print("Equal to equal operator for Tuple:",tuple1 ==tuple2)
print("Not equal to operator for Tuple:",tuple1 !=tuple2)

print("SET")
set1 = {1,5,7}
set2 = {5,7,6}
print("Less than operator for Set:",set1 < set2)
print("Greather than operator for Set:",set1 > set2)
print("Less than equal to operator for Set:",set1 <=set2)
print("Greather than equal to operator for Set:",set1 >=set2)
print("Equal to equal operator for Set:",set1 ==set2)
print("Not equal to operator for Set:",set1 !=set2)

# 3)Logical Operators: can be applied on all types
# Operator	                Description	                            Syntax
# and	    Logical AND: True if both the operands are true	       x and y
# or	    Logical OR: True if either of the operands is true 	   x or y
# not	    Logical NOT: True if the operand is false 	           not x

a = 23
b = 28
print("Logical operator for interger")
print("and operator for int",a and b)
print("or operator for int",a or b)
print("not operator for int", not b)


"""
6)Membership Operators:
Works on Sequence types string, tuple, list

in not in

"a" in "india" - True
"c" in "india" - False

"a" not in "india" - False
"c" not in :india" - True
"""
print("MEMBERSHIP OPERATORS")
fruits = ["watermelon","grapes","apple","banana","mango"]
print("mango" in fruits)

if "mango" in fruits:
    print("mango is a summer fruits")
else:
    print("mango fruit is not present")


data = [45,67,8,5,44,76,25,22,154]
print(8 in data)
print(75 not in data)

#for dictionary
data1 = {1:2, 3:4}
print(1 in data1)
print(2 in data1)

data = "happy holi"
print(data)
capital_holi = data.upper()
print(capital_holi)

"""
7) Identity Operators:
is     --> returns True is both operators point to same object,else False
is not --> returns False is both operator points to same object,else True
"""
print("IDENTITY OPERATORS")
n = 10
d = 10

print(n is d)

print(n is not d)

if n == d:
    print("Equal")

g =567
f = 567

print(g is f)

print(g is not f)

if g != f:
    print("not equal")
else:
    print("equal")










