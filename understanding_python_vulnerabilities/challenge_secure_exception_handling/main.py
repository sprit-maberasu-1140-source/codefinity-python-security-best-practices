def divide_numbers(a, b):
    try:
        return a/b
    except(ZeroDivisionError,TypeError):
        return "An error occurred. Please check your input."


output1 = divide_numbers(10, 2)
print(output1)
output2 = divide_numbers(10, 0)
print(output2)
output3 = divide_numbers(10, "x")
print(output3)