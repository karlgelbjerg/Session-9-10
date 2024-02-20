def greet(name):
    """
    simple greet function, prints hello
    :param name: string
    :return: None
    """
    print(f"Hello, {name}")


greet("Karl")
greet("Max")
greet("Tom")

def special_op(x, y, z):
    """
    some special operation
    :param x: int or float
    :param y: int or float
    :param z: int or float
    :return: the result of the operation
    """
    return x * y + z


result = special_op(2, 3, 4)
print(result)