from series import fibonacci, lucas, sum_series

# Fibonacci

def test_one():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_two():
    expected = 34
    actual = fibonacci(9)
    assert actual == expected

# Lucas

def test_three():
    expected = 3
    actual = lucas(2)
    assert actual == expected

def test_four():
    expected = 7
    actual = lucas(4)
    assert actual == expected

# sum_series

def test_five():
    expected = 3
    actual = sum_series(4)
    assert actual == expected