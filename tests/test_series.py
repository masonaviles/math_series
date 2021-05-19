from math_series import fibonacci, lucas, sum_series

# Fibonacci

def test_one():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_two():
    expected = 13
    actual = fibonacci(7)
    assert actual == expected

# Lucas

def test_three():
    expected = 29
    actual = lucas(7)
    assert actual == expected

# sum_series

def test_four():
    expected = 3
    actual = sum_series(4)
    assert actual == expected