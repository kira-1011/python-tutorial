import datetime


def logger(func):
    def wrapper():
        print(f"{datetime.datetime.now()} : {func.__name__}")
        func()

    return wrapper


@logger
def func1():
    print("func1")


@logger
def func2():
    print("func1")


func1()
func2()
