from lab.math_operation import add, multiply, subtract, divide


def perform_math_operation(inp):
    """
    """
    fn, sign, sn = inp.split()

    result = 0
    if sign == '+':
        result = add(float(fn), float(sn))
    elif sign == '*':
        result = multiply(float(fn), float(sn))
    elif sign == '-':
        result = subtract(float(fn), float(sn))
    elif sign == '/':
        result = divide(float(fn), float(sn))
    
    return result


print(perform_math_operation(input()))
