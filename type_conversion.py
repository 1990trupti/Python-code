num = 1
avg = 6.7
total = "500"
data = [5, 15, 35, 35, 45, 65, 15, 85, 95, 45, 55]
tuple_data = ("mango","watremelon","grapes","mango")
set1 = {1,2,3,4,5}


#implicit
print(type(num))
print(type(avg))
result = num + avg
print(type(result))

#explicit

#int conversion
print("float to int",int(avg))
print("float to int",int(78.455452125))
print("float to int",int(552480.14587))
print("str to int",int(total))
print("str to int",type(int("1245789622")))
print("float to int",int("5656593215486"))


#float conversion
# print("int to float", float(num))
# print("int to float", float(55))
# print("int to float", float(77754564687654))
# print("str to float", float(total))
# print("str to float", float("345.67"))
# print("str to float", float("45.268e"))


#str conversion
print("int to str", str(num))
print("int to str", str(4548521))
print("int to str", str(545455))
print("float to str", str(545.328))
print("float to str", str(452.2547))
print("float to str",str(data))

#converting list into string
string_list = ["mango","watremelon","grapes","mango"]
print("List to string",str(string_list))
print(" ".join(string_list))



#list conversion
# print("int to list", list(4))
# print("float to list",list(5.6))
print("string to list", list("INR"))
print("string to list",list("Welcome to Bit by Bit"))

# data = list(tuple_data)
# data.append("muskmelon")
# print("tuple to list",data)

# print("tuple to list",list(tuple_data))
# print("set to list", list(set1))

#tuple conversion:
print("string to tuple",tuple("welcome to Bit by Bit, STH"))
print("list to tuple",tuple(data))
print("set to tuple",tuple(set1))

#set conversion:
print("string to set",set("welcome to Bit by Bit, STH"))
print("list to set",set(data))
print("set to set", set(tuple_data))

#dictionary conversion:
dict_data = dict.fromkeys(tuple_data,"summer")
print(dict_data)

dict_list = dict.fromkeys((data))
print(dict_list)

dict_to_set = dict.fromkeys(set1)
print(dict_to_set)



dict_data = {1:2, 3:4, 5:6}

print(set(dict_data))
print(tuple(dict_data))
print(dict_data.keys())
print(dict_data.values())
print(dict_data.items())



#_______________________________
splitted_data = "Welcome to Bit by Bit, STH".split()
print(type(splitted_data))
splitted_data.append("python course")
print(splitted_data)