import operator
from functools import reduce
from itertools import accumulate


data = [45, 67, 89, 24, 56, 78, 98, 76, 45, 67, 87, 56]


result= reduce(operator.add,data)
print(result)

def greater(a, b):
    if a > b:
        return a
    else:
        return b

result= reduce(greater, data)
print(result)

result = list(accumulate(data,operator.add))
print(result)

result = list(accumulate(data, greater))
print(result)

# def capitalized_names(name):
#     names = name.split()
#     capital_list =[]
#     for nam in names:

def func(d):
    return d[1]

data = {"mango": 55,
        "apple": 100,
        "grapes": 75,
        "orange":44}

print(({k: v for k, v in sorted(data.items(), key=func)}))
