def test1(function, expected, parameter):
    print (function(parameter)==expected)
    return (function(parameter)==expected)

def test4(function, expected, i0, i1, i2, i3):
    print (function(i0, i1, i2, i3)==expected)
    return (function(i0, i1, i2, i3)==expected)


def distance(x0, y0, x1, y1):
    d = (x1 - x0)**2
    d = d + (y1 - y0)**2
    return d**0.5
test4(distance, 5.0, 3, 0, 0, 4)
test4(distance, 4, 3, 0, 0, 4)

def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp
test1(f_to_c, 100, 212.0)
test1(f_to_c, 212.0, 100)

def eval_quadratic(a, b, c, x):
    return a*x**2 + b*x + c
test4(eval_quadratic, 4, 1, 0, 3, 1)
test4(eval_quadratic, 7, 1, 0, 3, 1)

def is_even(n):
    return n % 2 == 0
test1(is_even, True, 2)
test1(is_even, True, 1)