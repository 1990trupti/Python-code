
def normal_function():
    data = list(range(500))
    n = 50
    i = 0
    n = 10

    for _ in range(50):
        yield data[i:n]
        i += 10
        n += 10

gen_obj = normal_function()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))

# for value in gen_obj:
#     print(value)


# def function():
#     pass
#
# print(1)
# function()
# print(2)
