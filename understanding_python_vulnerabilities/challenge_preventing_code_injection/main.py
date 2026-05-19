def safe_calculator(operation, a, b):
    allowed_operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else None
    }
    if operation in allowed_operations:
        result = allowed_operations[operation](a, b)
    else:
        result = None
    return result

res1 = safe_calculator("add", 2, 3)
print(res1)
res2 = safe_calculator("divide", 10, 2)
print(res2)
res3 = safe_calculator("power", 2, 3)
print(res3)
res4 = safe_calculator("divide", 5, 0)
print(res4)
