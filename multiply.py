def multiply(x, y):
    """Simple function returns the sum of the arguments"""
    return x * y

def my_map(func, arg1, arg2):
    """
    This will map the function 'func' to each pair
    of arguments in the lists 'arg1' and 'arg2', returning the result
    """
    res = []  # Output
    for i, j in zip(arg1, arg2):
        res.append(func(i, j))
    return res

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
result = my_map(multiply,a, b)
print(result)
