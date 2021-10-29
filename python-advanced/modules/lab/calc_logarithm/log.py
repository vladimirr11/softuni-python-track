from math import log


def calc_log(b, x):
    """
    """
    return f'{log(x):.2f}' if b == 'natural' else f'{log(int(x), int(b)):.2f}'
