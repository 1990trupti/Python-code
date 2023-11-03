from itertools import zip_longest

# --------------------enumerate---------------------------

# data = ["name", "age", "height", "weight"]
# data1 = ["ashok", 45, 5.6, 67]

# for ind, item in enumerate(data,0):
#     print(item)
#     print(data1[ind])
#     print()


# -------------------zip----------------------------
# data = ["name", "age", "height", "weight"]
data1 = ["ashok", 45, 5.6, 67]
# data2 = ["mahesh", 56, 5.5, 65, 100, 200]
data3 = ["a","b","C","d","e","f","g","h"]

# result = list(zip(data,data1,data2))
# print(result)

# for item in zip(data,data1,data2):
#     print(item)

# ------------------zip-longest--------------------
# result = list(zip_longest(data,data1,data2,data3, fillvalue="***"))
# print(result)


# ---------------------filter----------------------
data4 = ["ashok", "45", "5.6", "67", "abcdef"]
# result = list(filter(str.isalpha,data4))
# print(result)

def is_prime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
        else:
            return True
#
# data = list(range(2,2000,7))
# result = list(filter(is_prime, data))
# print(result)
#
# data2 = ["mahesh", 56, 5.5, 65, 100, 200]
# prime = []
# for item in data2:
#     if is_prime(item):
#         prime.append(item)
# print(prime)

# ---------------map---------------------

def capitalized_names(name):
    names = name.split()
    capital_list = []
    for nam in names:
        s = nam[0].capitalize() + nam[1: ]
        capital_list.append(s)
    print(capital_list)
    return " ".join(capital_list)

names = ["sachin tendulkar","brian lara","ricky ponting","glenn mcGrath","ryan benNon mcDonald"]

result = list(map(capitalized_names, names))
print(result)

nums = [45456.4545,4523.67867645,786.234,8765.1234]
decimal = [1, 2, 3, 4]

result = list(map(round, nums, decimal))
print(result)

result = list(map(is_prime,[23,34,45,44]))
print(result)

round(nums[0],decimal[0])
round(nums[1],decimal[1])
round(nums[2],decimal[2])
round(nums[3],decimal[3])

def mtest_map_filter(a,b,c,d):
    pass



# result=[]
# for item in names:
#     op = capitalized_names(item)
#     result.append(op)
# print(result)