# should have one parameter n. The function should return the nth value in the fibonacci series using recursion or iteration.
def fibonacci(fib_n):
    if fib_n == 0:
        return 0
    elif fib_n == 1:
        return 1
    else:
        return fibonacci(fib_n - 1) + fibonacci(fib_n - 2)

# returns the nth value in the lucas numbers
def lucas(lucas_n):
    if lucas_n == 0:
        return 2
    elif lucas_n == 1:
        return 1
    else:
        return lucas(lucas_n - 1) + lucas(lucas_n - 2)

# with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.
def sum_series(required_n, zero=0, one=1):
    if required_n == 0:
        return zero
    if required_n == 1:
        return one
    return sum_series(required_n - 1, zero, one) + sum_series(required_n - 2, zero, one)