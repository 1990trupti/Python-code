#string and its methods

s1 = "goOd"
s2 = "morning"
s3 = "today is thursday"
s4 = "02/03/2023"
s5 = "192.168.1.1"
s6 = "i scream you scream we all scream for ice cream"

#___________________________________________
#string concatination() - add strings together, use the + character to add a variable to another variable
print("CONCATINATION")
concatenated_string = s1 +" "+ s2
print(concatenated_string)

#________________________
#string multiplication() - use '*' operator, string to be copied with the required number of times
print("MULTIPLICATION")
data = "&^%$#" * 5
print(data)

print(s1 * 4)
print("#" * 15)

#_________________________________________
#capitalize() - capitalizaes first character of the string

print("CAPITALIZATION")
print(s1.capitalize())


#title()- capitalize the first letter of every words
print("TITLE")
print(s3.title())
print(s6.title())

#upper - capitilizer entire string
print("UPPER")
print(s1.upper())
print(s3.upper())

#lower - lower the entire string
print("LOWER")
print(s1.lower())
print(s6.lower())

#length -
print("LENGTH")
print(len(s1))
print(len(s3))

s1 = "goOd"
s2 = "morning"
s3 = "today is thursday"
s4 = "02/03/2023"
s5 = "192.168.1.1"
s6 = "i scream you scream we all scream for ice cream"

#_____________________________________________
#startswith() - checks if string starts with the specified string
print("STARTSWITH")

print(s2.startswith("To"))
print(s3.startswith("to"))

sent = "phising attack was observed on email test@gmail.com"
# sent = "malware attack was observed on email test@gmail.com"
# sent = "ddos attack was observed on email test@gmail.com"


print(sent.startswith("phising"))
print(sent.startswith("malware"))
print(sent.startswith("ddos"))


# if sent.startswith(("phising")):
#     print("phishing attack occured")
#
# if sent.startswith("malware"):
#     print("phishing attack occurred")
#
# if sent.startswith("dddos"):
#     print("phishing attack occurred")

#____________________________________________
#endswith() -returns false if the string does not ends with given value

print("ENDSWITH")
print(s3.endswith("day"))

#____________________________________
#split - splits the string into a list by the given seperator

s1 = "goOd"
s2 = "morning"
s3 = "today is thursday"
s4 = "02/03/2023"
s5 = "192.168.1.1"
s6 = "i scream you scream we all scream for ice cream"

print("SPLIT")
print(s3.split())
print(s6.split())
print(s1.split())
print(s4.split("/"))

#_________________________________________
path = "D:/practise_code/basic/string_implementation.py"

splitted_data = path.split("/")
print(splitted_data)
# file_name = splitted_data[-1]
# print(file_name)
# ext = file_name.split(".")
# print(ext)
# file_name1 = ext[-1]
# print(file_name1)

#_________________________________________________________________________
# join() - returns a concatenated string

print("JOIN:")
data = ['i', 'scream', 'you', 'scream', 'we', 'all', 'scream', 'for', 'ice', 'cream']

print(" ".join(data))

path_data = ['D:', 'practise_code', 'basic', 'string_implementation.py']
path = "/".join(path_data)
print(path)

#___________________________________________________________________________
#isalpha() -  checks if all characters are alphabets
s1 = "goOd"
s2 = "morning"
s3 = "today is thursday"
s4 = "02/03/2023"

print("ISALPHA:")
print(s2.isalpha())
print(s3.isalpha())

#_________________________________________________
#isalnum() - checks Aphanumeric character
# not alphabet letters:(space)!#%&? etc.

print("ISALNUM:")
pancard = "GTAG47A"
print(pancard.isalnum())

#_________________________________________________________________________
#isdecimal() - checks Decimal charaters. returns True if all the characters are decimals (0-9).
# This method is used on unicode objects.
print("ISDECIMAL")
text = "\u0033"  # unicode for 3
print(text.isdecimal())

#________________________________________________________________________________
#isidentifier() - checks for valid Identifier. A string is considered a valid identifier
# if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
# A valid identifier cannot start with a number, or contain any spaces.
print("ISIDENTIFIER:")
data = "DATAof_50"
data1 = "45data$"
print(data.isidentifier())
print(data1.isidentifier())

#__________________________________________________________
#islower() - checks if all Alphabets in a string are Lowercase
# Numbers, symbols and spaces are not checked, only alphabet characters.

s1 = "goOd"
s2 = "morning"
s3 = "today is thursday"
s4 = "02/03/2023"
print("ISLOWER:")
print(s1.islower())
print(s2.islower())

#________________________________________________________________
#isnumeric() - checks numeric characters
print("ISNUMERIC:")
sum = "4752486"
print(sum.isnumeric())

#__________________________________________________________________________
#isprintable() - checks printable characters
txt = "माझं नाव तृप्ती आहे."
txt1 = "hello /n"
print("ISPRINTABLE:")
print(txt)
print(txt1.isprintable())

#____________________________________________________________________________________
#isspace() - returns True if all the characters in a string are whitespaces,otherwise False.
# checks whitespcae characters

s2 = "morning"
s3 = "today is thursday"
s4 = "02/03/2023"
data = "     "
print("ISSPACE:")
print(s2.isspace())
print(s3.isspace())
print(data.isspace())
#_______________________________________________________________________________
#istitle() - check if each word start with an upper case letter:

data = "My Name Is Trupti"
print("ISTITLE")
print(s3.istitle())
print(data.istitle())

#__________________________________________________________
#isupper() - returns if all characters are uppercase characters

data = "ABCDEFGH"
print(("ISUPPER"))
print(s1.isupper())
print(data.isupper())

#_______________________________________________________________


#++++++++++++++++++++++++++++++++++++++++++
checklist = ["form", "id", "email", "photo"]

# str1 = "form"
# if str1 in checklist:
#     print("valid")       it will give valid because form is present in checklist

# str1 = "Form"
# print("*****")
# if str1.lower() in checklist:
#     print("valid")
# print("*****")

checklist = ["form", "Id", "email", "photo"]
# checklist = [item.lower() for item in checklist] #take one word and lower that word
# print(checklist)


# str1 = "Form"

# for item in checklist:
#     if str1.lower() == item.lower():
#         print("valid")
#         print("form is good")
#______________________________________________

checklist = ["form", "Id", "email", "photo"]

str1 = "Form"
# for item in checklist:
#      if str1.lower() == item.lower():
#          print("valid")
#          print("form is good")
#          print("please share your id")
#          print("please share your photo")

# for item in checklist:
#     print("for scope line1")
#     if str1.lower() == item.lower():
#          print("valid")
#          print("if scope line 2")
#          print("if scope line 3")
#          print("if scope line 4")
#          print("after if for scope line1")
#          print("after if for scope line2")
#          print("after if for scope line3")
# print("end for scope")




#_____________________________________________




#3/3/2023
#find(<sub_str>,start,end) - returns the index where


# s6 = "i scream you scream we all scream for ice cream"
# print(s6.find("scream"))
# print(s6.find("scream",10 ,40))




# count<substr>,start,end)

# print(s6.count("scream",0,10))
# print(s6.count("scream",0,4))

#replace(<old_str>,<new_str>)

# print(s6.replace("scream","cream"))
#
# kj = "miss Kajol"
# print(kj.replace("miss","mrs"))
#______________________________________

# email = "test123@gmail.com"
# print(email)

# s = "785421635"
# print("+91"+ s)

#isidentifier() -

#max = 60
#ma x = 89
#1min = 55
# print("max".isidentifier())
# print("min".isidentifier())
# print("ma x".isidentifier())
# print("1min".isidentifier())










