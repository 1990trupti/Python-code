
# Python dir() Function:--  Returns list of the attributes and methods of any object
# Syntax------- dir(object)
# object------	The object you want to see the valid attributes of
print("__________________________________")
class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))

# ____________________________________________________________________________________________________
#Python abs() Function---- The abs() function returns the absolute value of the specified number.
# syntax---- abs(n)
# n-------	Required. A number
print("________________________________________________")
x = abs(3+5j)
print(x)


# ___________________________________________________________________________________________________________________________
# Python all() Function----The all() function returns True if all items in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the all() function also returns True.
# syntax-----all(iterable)
# iterable------	An iterable object (list, tuple, dictionary)

print("____________________________________________________")
mylist = [True, True, True]
x = all(mylist)
print(x)

mylist = [0, 1, 1]
x = all(mylist)
print(x)
# Returns False because 0 is the same as False

mytuple = (0, True, False)
x = all(mytuple)
print(x)
# Returns False because both the first and the third items are False

myset = {0, 1, 0}
x = all(myset)
print(x)
# Returns False because both the first and the third items are False

mydict = {0 : "Apple", 1 : "Orange"}
x = all(mydict)
print(x)
# Returns False because the first key is false.
# For dictionaries the all() function checks the keys, not the values.


# __________________________________________________________________________________________________________________________
# Python any() Function---The any() function returns True if any item in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the any() function will return False.
# syntax---any(iterable)
# iterable-----	An iterable object (list, tuple, dictionary)

print("____________________________________")
mylist = [False, True, False]
x = any(mylist)
print(x)

mytuple = (0, 1, False)
x = any(mytuple)
print(x)
# Returns True because the second item is True

myset = {0, 1, 0}
x = any(myset)
print(x)
# Returns True because the second item is True

mydict = {0 : "Apple", 1 : "Orange"}
x = any(mydict)
print(x)
# Returns True because the second key is True.
# For dictionaries the any() function checks the keys, not the values.


#_________________________________________________________________________________________________________________________
# Python ascii() Function------The ascii() function returns a readable version of any object (Strings, Tuples, Lists, etc).
# The ascii() function will replace any non-ascii characters with escape characters:
# å will be replaced with \xe5.
# syntax----ascii(object)
# object-------	An object, like String, List, Tuple, Dictionary etc.

print("_____________________________________________________________")
x = ascii("My name is Ståle")
print(x)

# _____________________________________________________________________________________________________________
#Python bin() Function-----The bin() function returns the binary version of a specified integer.
# The result will always start with the prefix 0b.
# syntax-----bin(n)
#n-----	Required. An integer

print("__________________________________________________")
x = bin(36)
print(x)
# The result will always have the prefix 0b


# ________________________________________________________________________________________
# Python bool() Function------The bool() function returns the boolean value of a specified object.
# The object will always return True, unless:
# The object is empty, like [], (), {}
# The object is False
# The object is 0
# The object is None
# syntax----bool(object)
# object	Any object, like String, List, Number etc.

print("____________________________________________________")
x = bool(1)
print(x)

# _____________________________________________________________________________________________
# Python bytearray() Function----The bytearray() function returns a bytearray object.
# It can convert objects into bytearray objects, or create empty bytearray object of the specified size.

# syntax----bytearray(x, encoding, error)

# x--------	A source to use when creating the bytearray object.
#If it is an integer, an empty bytearray object of the specified size will be created.
# If it is a String, make sure you specify the encoding of the source.
# encoding-----	The encoding of the string
# error--------	Specifies what to do if the encoding fails.

print("____________________________________________")
x = bytearray(4)
print(x)


# Python bytes() Function-----The bytes() function returns a bytes object.
# It can convert objects into bytes objects, or create empty bytes object of the specified size.
# The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified,
# and bytearray() returns an object that can be modified.

# syntax---bytes(x, encoding, error)
# x	-------A source to use when creating the bytes object.
# If it is an integer, an empty bytes object of the specified size will be created.
# If it is a String, make sure you specify the encoding of the source.
# encoding-----	The encoding of the string
# error	-------Specifies what to do if the encoding fails.
print("_______________________________")
print("Python bytes() Function")
x = bytes(4)
print(x)

# ____________________________________________________________________________________________________________________
# Python callable() Function-----The callable() function returns True if the specified object is callable, otherwise it returns False.
# syntax--------callable(object)
# object	The object you want to test if it is callable or not.


print("_____________________________________")
print("Python callable() Function")
def x():
    a = 5
print(callable(x))

x = 5
print(callable(x))


# __________________________________________________________________________________________________
# Python chr() Function-----The chr() function returns the character that represents the specified unicode.
# syntax-----chr(number)
# number-------	An integer representing a valid Unicode code point

print("_______________________________")
print("Python chr() Function")
x = chr(97)
print(x)


# _________________________________________________________________________________________
# classmethod()	-------- Converts a method into a class method


# ______________________________________________________________________________________
# Python compile() Function----The compile() function returns the specified source as a code object, ready to be executed.

# syntax----compile(source, filename, mode, flag, dont_inherit, optimize)

# source	Required. The source to compile, can be a String, a Bytes object, or an AST object
# filename	Required. The name of the file that the source comes from. If the source does not come from a file, you can write whatever you like
# mode	Required. Legal values:
# eval - if the source is a single expression
# exec - if the source is a block of statements
# single - if the source is a single interactive statement
# flags	Optional. How to compile the source. Default 0
# dont-inherit	Optional. How to compile the source. Default False
# optimize	Optional. Defines the optimization level of the compiler. Default -1

print("_______________________________________________")
print("Python compile() Function:")
# syntax----compile(source, filename, mode, flag, dont_inherit, optimize)
x = compile('print(55)', 'test', 'eval')
exec(x)

x = compile('print(55)\nprint(88)', 'test', 'exec')
exec(x)


# _____________________________________________________________________________________
#Python complex() Function-----The complex() function returns a complex number by specifying a real number and an imaginary number.
# complex(real, imaginary)

# real	Required---------A number representing the real part of the complex number. Default 0.
# The real number can also be a String, like this '3+5j', when this is the case, the second parameter should be omitted.
# imaginary	Optional------------- A number representing the imaginary part of the complex number. Default 0.

print("_______________________________________")
print("Python complex() Function:")
x = complex(3, 5)
print(x)

x = complex('3+5j')
print(x)

# ____________________________________________________________________________________
# Python delattr() Function---The delattr() function will delete the specified attribute from the specified object.
# syntax----delattr(object, attribute)
# object-------	Required. An object.
# attribute--------	Required. The name of the attribute you want to remove

print("_________________________________________________")
print("Python delattr() Function:")
class Person:
  name = "John"
  age = 36
  country = "Norway"
delattr(Person, 'age')

# The Person object will no longer contain an "age" property

# _______________________________________________________________________________________
#Python dict() Function---The dict() function creates a dictionary.
# A dictionary is a collection which is unordered, changeable and indexed.
#syntax----- dict(keyword arguments)
# keyword arguments	Optional. As many keyword arguments you like, separated by comma: key = value, key = value ...


print("_________________________________________")
print("Python dict() Function:")
x = dict(name = "John", age = 36, country = "Norway")
print(x)

# ______________________________________________________________________________________
#Python divmod() Function---The divmod() function returns a tuple containing the quotient
# and the remainder when argument1 (dividend) is divided by argument2 (divisor).

# syntax---divmod(dividend, divisor)

# dividend---------	A Number. The number you want to divide
# divisor----------	A Number. The number you want to divide with
print("___________________________________________________")
print("Python divmod() Function")
x = divmod(5, 2)
print(x)


# ________________________________________________________________________________________
# Python enumerate() Function----- The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.

# syntax ----- enumerate(iterable, start)

# iterable	An iterable object
# start	A Number. Defining the start number of the enumerate object. Default 0

print("______________________________________")
print("Python enumerate() Function")
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y))

# _________________________________________________________________________________________________
#Python eval() Function---The eval() function evaluates the specified expression,
# if the expression is a legal Python statement, it will be executed.
# syntax---eval(expression, globals, locals)
# expression	A String, that will be evaluated as Python code
# globals	Optional. A dictionary containing global parameters
# locals	Optional. A dictionary containing local parameters


print("_________________________________________")
print("Python eval() Function")
x = 'print(55)'
eval(x)

# __________________________________________________________________________
# Python exec() Function-----The exec() function executes the specified Python code.
# The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression

# syntax-----exec(object, globals, locals)

# object-------	A String, or a code object
# globals------	Optional. A dictionary containing global parameters
# locals-------	Optional. A dictionary containing local parameters

print("______________________________________________")
print("Python exec() Function")
x = 'name = "John"\nprint(name)'
exec(x)

# ___________________________________________________________________________________
#Python filter() Function----The filter() function returns an iterator where the items are filtered
# through a function to test if the item is accepted or not.
# syntax---filter(function, iterable)
# function	A Function to be run for each item in the iterable
# iterable	The iterable to be filtered

print("_____________________________________________")
print("Python filter() Function:")
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages)
for x in adults:
  print(x)

# ____________________________________________________________________________________
#Python float() Function---- The float() function converts the specified value into a floating point number.
# syntax-----float(value)
# value	A number or a string that can be converted into a floating point number

print("________________________________________")
print("Python float() Function:")
x = float(3)

print(x)

x = float("3.500")

print(x)


# __________________________________________________________________________________________________________
#Python format() Function------The format() function formats a specified value into a specified format.
# syntax-------format(value, format)
# value----	A value of any format
# format-------	The format you want to format the value into.
# Legal values:
# '<' - Left aligns the result (within the available space)
# '>' - Right aligns the result (within the available space)
# '^' - Center aligns the result (within the available space)
# '=' - Places the sign to the left most position
# '+' - Use a plus sign to indicate if the result is positive or negative
# '-' - Use a minus sign for negative values only
# ' ' - Use a leading space for positive numbers
# ',' - Use a comma as a thousand separator
# '_' - Use a underscore as a thousand separator
# 'b' - Binary format
# 'c' - Converts the value into the corresponding unicode character
# 'd' - Decimal format
# 'e' - Scientific format, with a lower case e
# 'E' - Scientific format, with an upper case E
# 'f' - Fix point number format
# 'F' - Fix point number format, upper case
# 'g' - General format
# 'G' - General format (using a upper case E for scientific notations)
# 'o' - Octal format
# 'x' - Hex format, lower case
# 'X' - Hex format, upper case
# 'n' - Number format
# '%' - Percentage format

print("_______________________________________________-")
print("Python format() Function:")
x = format(0.5, '%')
print(x)

x = format(255, 'x')
print(x)


# ________________________________________________________________________________________________-
#Python frozenset() Function-----The frozenset() function returns an unchangeable frozenset object
# (which is like a set object, only unchangeable).
# syntax-----frozenset(iterable)
# iterable	An iterable object, like list, set, tuple etc.


print("____________________________________________________")
print("Python frozenset() Function:")
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)

# mylist = ['apple', 'banana', 'cherry']
# x = frozenset(mylist)
# x[1] = "strawberry"
# print(x)

# ______________________________________________________________________________________
# Python getattr() Function------The getattr() function returns the value of the specified attribute from the specified object.
# syntax-----getattr(object, attribute, default)
# object	Required. An object.
# attribute	The name of the attribute you want to get the value from
# default	Optional. The value to return if the attribute does not exist

print("____________________________________________________________")
print("Python getattr() Function")
class Person:
  name = "John"
  age = 36
  country = "Norway"
x = getattr(Person, 'age')
print(x)

class Person:
  name = "John"
  age = 36
  country = "Norway"
x = getattr(Person, 'page', 'my message')
print(x)



















































































