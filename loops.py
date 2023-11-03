# loops are features thats can be used to some task repetatively.
#For loop
# sytanx:
# for <var_name> in <iterable>:
    # line1
#     line2
# line3
# .
# .
# line n


# for i in range(1, 11):
#     print("Occurence no:", i)
#     print("****")
#     print(i+10)


#
# tod = [5, 2 , 1, 10, 100, 50, 500, 20, 1000]

# for loop on set
# s1 = {10, 20, 30, 40, 50}
#
# for item in s1:
#     print(item)
#
# # for loop on strings
# message = "Good morning"
# for item in message:
#     print(item)
#
# #for loop on dictionary
# person_rollnumber = {"atul": 1,"Rakesh": 54, "diti": 47}

#

# _______________________________________________________
# ______________________________________
# while loops - we can execute a set of statements as long as condition is true.
# syntax - while <condition>
#            blocks

# ________________________________________
# while True:
#     print("Inside while loop")
#     print("second line of while loop")

# i = 0
# while i < 10:
#     print(i)
#     i += 1
#
# i = 0
# while True:
#     d = input("Enter the passcode")
#     if d == "six":
#         print("Entry Allowed")
#         break
#
#     if i==5:
#         print("retries exhausted")
#         break
#     i+=1


# i = 1
# j = 1
# while j < 11:
#     print(f"{i} * {j} = {i*j}")
#     j+=1


# while True:
#     num = int(input("Enter a number"))
#     if num%2 == 0:
#         break

# n1 = 10
# n2 = 40
# print(f"{n1*n2} is multiplictaion of {n1} and {n2}")


#
# n = int(input("Enter a number"))
# i = 2
# while i < n:
#     if n%i == 0:
#         print("Not Prime")
#         break
#     i+=1
# else:
#     print("Prime")
#
#
# for item in ["mango","grapes","watermelon","muskmelon"]:
#     print("item")
# else:
#     print("something")


# Input:
# X = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# Y = [[9, 8, 7],
#      [6, 5, 4],
#      [3, 2, 1]]
#
# Output:
# result = [[10, 10, 10],
#           [10, 10, 10],
#           [10, 10, 10]]


print("Python program to add two Matrices")
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)





































