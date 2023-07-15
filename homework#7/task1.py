def calculate_factorial(n):
    """calculates the factorial of a certain number"""
    result = 1
    for i in range(1, n+1):
        result = result * i

    return result


print(calculate_factorial(5))


def factorial_recursion(n):
    """calculates the factorial of a certain number using a recursion"""
    if n == 1:
        return 1
    else:
        return n * factorial_recursion(n-1)


print(factorial_recursion(5))


def factorial_generator(n):
    """calculates and yields the factorials of all numbers through a certain number"""
    result = 1
    for i in range(1, n + 1):
        result = result * i
        yield result


for x in factorial_generator(5):
    print(x)



