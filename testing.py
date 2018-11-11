from logger import Logger


@Logger("111", "log")
def suma(a, b):
    return a + b


s = suma(1, 2)