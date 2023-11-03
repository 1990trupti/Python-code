

# *args and **kwargs

def function_name(param_1, *args, **kwargs):
    print("value pf param_1 is",param_1)
    print("value of args is", args)
    print("value of kwargs",kwargs)

function_name("Monday",1,2.5,"test", a=10,b=20,c=30)
print("__________________")
function_name("Monday")
print("_____________________")
function_name("Monday", 1, a=10,b=20,c=30)
print("__________________________")
function_name("Monday", 1, 2.5,5,8,7,56,"test", a=10,i=85,h=99)

# arbitory no of position arguments - *args
# arbitary number of keyword arguments - **kwargs

print("**************************************************")
# def function_name(param_1, *args, **kwargs):
#
# def total(*args):
#     sum = 0
#     for item in  args:
#         sum+=item
#     return sum

def total(initial_value, *args):
    for item in args:
        initial_value += item
    return initial_value

print(total(1,2,3,5))
print(total(45,85,66,85))
print(total(1,0))

def example(**kwargs):
    pass

def example(*args,**kwargs):
    pass

print("*********************************")

def with_some_other_params(param1, *args, param2, param3=30, **kwargs):
    print(param1)
    print(args)
    print(param2)
    print(param3)
    print(kwargs)

with_some_other_params(10,20,30,40,50,param2=60,param3=65, a=10,b=20)

print("***********************************")
def names(*kuch_bhi, **iska_bhi_kushbhi):
    print(kuch_bhi)
    print(iska_bhi_kushbhi)
names(1,2,3,a=10,b=20,c=30)

names(1,2,3, age=30, height=5.4,weight=200)











