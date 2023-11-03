"""List:[1,2,3,4,5]
    * Backed by Array
    * Index Based - start from 0 - Index can be Positive and Negative -
      Positive Index >=0, Negative Index, <=-(Length)
    * # E.g.: a[-2] is a[length-2]
    * Holds homogeneous(meanining: made of same type of things) + heterogeneous(differents) data elements(For Hetro Every
      element is treated as Object)
    * Mutable - can append/add/replace/remove/update
    * Sequence Order is Preserved
    * Duplicates are Allowed
    * Multiple None Type Allowed
    * Ideal for searching and retrieval
    *Insertion and Deletion are costly operations

inbuilt methods: append,insert,extend,copy,count,reverse,sort,pop
                 remove,clear,index
"""

example = [1,2,3,4,"one","two",2.5,True]
# print(example[2])
print(example)
example.pop(2)
print(example)
print(example[-2])

#___________________________________
# type_of_denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
# cellphone_accessories = ["headphone", "cover", "screenguard", ["charging_adapter","charging_cable"],"smart_watch"]
# travel_checklist = ["bag", "charger", "food", "umbrella", "watch"]
# print(cellphone_accessories[-2][0])
#______________________________________________

#list data
type_of_denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

#accessing using index

#positive
print(type_of_denominations[4])
twenty = type_of_denominations[4]
sum = type_of_denominations[5]+type_of_denominations[2]

#negative
print(type_of_denominations[-2])
last_second_element = type_of_denominations[-2]

#Operations on List Datatype which called as methods
#inbuilt methods: append,insert,extend,copy,count,reverse,sort,pop,clear

#append - adds the given element at the end of the list
#syntax - variable_name_list.append(<element>)

type_of_denominations.append(2000)
print(type_of_denominations)

#extend -extends the current list with the elemnts of given list
#syntax - variable_name_list.extend(<element>)

digital_currency = ["phonePay", "Google", "BharatPe"]
type_of_denominations.extend(digital_currency)
print("List after extending digital urrency:", type_of_denominations)

#____________________

#insert - add the element at the given index
#syntax- variable_name_list.insert(<index>,<element>)

type_of_denominations.insert(7, 200)
print("after inserting element at 7th index:",type_of_denominations)
print(len(type_of_denominations))


#_____________________________________________
#count - returns the count of given element inside the list
#syntax - variable_name_list.count(<element>)

print("count of 500:", type_of_denominations.count(500))
print("count of 100:", type_of_denominations.count(100))
print("count of 200:", type_of_denominations.count(200))
#__________________________

#index - returns the index of given element from the list
#syntax - variable_name_list.index(<element>)

print("index of 500:", type_of_denominations.index(500))
print("index of 2:", type_of_denominations.index(2))
print("index of 100:", type_of_denominations.index(100))
print(type_of_denominations[8])

#______________________________________

#pop - removes the last element from the list and return that element
# syntax - variable_name_list.pop()

last_element = type_of_denominations.pop()
print(type_of_denominations)
print(last_element)

print(type_of_denominations.pop())
print(type_of_denominations)

print(type_of_denominations.pop())

#_______________________________________

#remove - remove the given element from the list if present, if not present will raise the error(exception)
#syntax - variable_name_list.remove(<element>)

type_of_denominations.remove(1000)
print(type_of_denominations)

#________________________________________________-

#reverse - reverse the given list
#syntax - variable_name_list.reverse()

type_of_denominations.reverse()
print("after reversed:", type_of_denominations)

#___________________________________________
#sort - will sort the given list
#syntax - variable_name_list.sort()

print(type_of_denominations)

# print(type_of_denominations.sort())

# type_of_denominations.sort()
# print(type_of_denominations)

#
# type_of_denominations.sort(reverse=True)
# print(type_of_denominations)
#
# fruits = ["mango", "grapes", "apple", "banana", "watermelon"]
# fruits.sort()
# print(fruits)

#_______________________________
# copy - copy the list
# syntax - variable

copy_of_type_of_denominations = type_of_denominations.copy()
print("original", type_of_denominations)
print("copies", type_of_denominations)

type_of_denominations.append(5000)
copy_of_type_of_denominations.insert(6, 75)

print("original", type_of_denominations)
print("copies", copy_of_type_of_denominations)

#_____________________________________
#clear - clear the list

type_of_denominations.clear()
print("After CLear", type_of_denominations)

type_of_denominations.append(1)
print(type_of_denominations)

#__________________________________________-