# range(start,stop,step) - generate svalues

# range(5) - 0,1,3,4
# range(1,10) - 1,2,3,4,5,6,7,8,9
# print(list(range(0,100,5)))
#
# for num in range(1,11):
#     print(num)
#
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print()
# print("______________")

#nested loops - loop inside a loop is called nested loops
# for each iteration of outer loop, inner loop runs completely

# i = 1
# while i < 11:
#     j = 1
#     while j < 6:
#         print(f"{i} * {j} = {i*j}")
#         j+=1
#     print()
#     i+=1

# list comprehesion - shortcut way of generating list

# syntax [var for var in <iterable]


# data = [var for var


weakdays =("Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturady","Sunday")
data = list(weakdays)
print(data)

capital_days = [day.upper() for day in weakdays]
capital_days =[]
for day in weakdays:
    capital_days.append(day.upper())
print(capital_days)

# write a program that will print a list of even numbers less than 101
# even_numbers = []
#
# for num in range(1,101):
#     if num%2 == 0:
#         even_numbers.append(num)
# print(even_numbers)


even_list = [num for num in range(1,101) if num%2==0]
print(even_list)

#set comprehension
# dictionary comprehesion

data = {num for num in range(1,11)}  #set
person = {"name":"Rakesh", "Lastname":"Shah",
          "age":45, "weight":"56","height":5.7,
          "BMI":5.7,"fav_color":"black"}
data = {key:value for key,value in person.items()}
print(data)


data= {char:ord(char) for char in "Friday"}
print(data)



















