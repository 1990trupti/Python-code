from functools import wraps

def outer(func):

    @wraps(func)
    def inner(*args, **kwargs):
        print("-------------------------------")
        print("This is will be before original function")
        func(*args, **kwargs)
        print("This is will be after original function")
        print("------------------------------------------")
    return inner()

@outer
def remove_duplicated_without_set():
    data = [43.54,85,44,21,65,85]
    for item in data:
        count = data.count(item)
        if count > 1:
            for _ in range(count-1):
                data.remove(item)
    data.sort()
    print(data)





