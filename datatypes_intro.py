"""Booelan:
        keyword: bool
        Description: A Boolean value of either True or False
        In Python Boolean is also and int, basically bool is a subclass of int and has only two possibilities.
        True and False which is 1 or 0.
        Can perform logical operations and,or,not.
        If arithmatic operations are done on Boolean. Then 1 and 0 is used to obtain result.
        True + False -> 1+0=1
        True* False -> 1*0=0
        True * False -> 1*0=1 """

enabled = True
disabled =  False

internet_connection_stable = True

if internet_connection_stable:
    print("Start joining the session o time")

print(True + False)
print(False + False)

#___________________________________________________________________________________

#Numbers : int, float, complex
#int

num = 10
month =  2
day = 2
temperature = 18
participants = 9

a1 = 45
a2 = 85
a3 = 77
avg = (a1 + a2 + a3)/3
print(avg)

girl_1 = 45
girl_2 =60
print(girl_1>girl_2)

#budget = 2000000000000
budget = 2.e12
print(budget)


#float

time = 8.30
date = 21.2
weight = 78.5
average = 55.2

#complex
# keyword:complex
x=2+1j
y=3+4j
print(x)
print(y)
print(x+y)

#string
# keyword:str

today = "Tuesday"
month = "February"
message = "Bit by bit make success your Habit"
org = "Bit by Bit"
doc = """This is first line
this is second line"""

print(today)
print(month)
print(message)
print(today.upper())
print(today.count('d'))

print(0b10)

# string ch escape
# Specifying a backslash (\) in front of the quote character in a string “escapes” it and causes
# Python to suppress its usual special meaning
print('a\....b')

print("mrcet is an autonomous (\') college")

print('a\
....b')

print('a\
b\
c')

print('a \n b')

print("mrcet \n college")

print("a\tb")





