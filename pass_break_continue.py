

# pass = just to pass the execution
# break = breaks the loops
# continue = continue the iteration

if True:
    pass

def sod():
    pass

pass

odd_list = []
for i in range(10):
    if i%2==0:
        pass
    else:
        odd_list.append(i)
print(odd_list)



for i in range(1,11):
    for j in range(1,11):
        print(i*j)
        if j%5==0:
            break




for i in range(1,11):
    if i == 3:
        break

    for j in range(1,11):
        print(f"{i}*{j} = {i*j}")
        if j%5==0:
            break

    print()
print("outer exit")


# for i in range(1,11):
#
#     for j in range(1,11):
#         print(f"{i}*{j} = {i*j}")
#         if j%5==0:
#             continue
#
#     print()
# print("outer exit")













