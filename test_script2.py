"""Code for practicing decorators"""

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("starting")
        func(*args, **kwargs)
        print("ending")
    return wrapper

@my_decorator(2)
def add(x, y):
    result = x+y
    print(result)

add(2, 8)