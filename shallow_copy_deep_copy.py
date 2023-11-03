
import copy

data = {"days": ["monday", "tuesday", "wednesday"],
        "months":["jan", "feb", "march"]}

# Shallow copy
data_copy = data

# data1 = data.copy()
# data1 =  copy.copy(data)

# print(data)
# print(data1)
#
# data1.update({"festival":"Ganesh chaturthi"})
# data1["days"].append("thursday")
# data1["months"].append("apr")
#
# print(data)
# print(data1)

#Deep copy---
data1 = copy.deepcopy(data)

print(data)
print(data1)

data1.update({"festival":"Ganesh chaturthi"})
data1["days"].append("thursday")
data1["months"].append("apr")

print(data)
print(data1)
