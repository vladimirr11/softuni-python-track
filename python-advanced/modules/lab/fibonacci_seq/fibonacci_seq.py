def create_seq(end_num):
    """
    """
    fib_seq = [0, 1]
    for i in range(2, end_num):
        result = fib_seq[i - 1] + fib_seq[i - 2]
        fib_seq.append(result)

    return fib_seq


def locate(fib_seq: list, num: int):
    """
    """
    result = ''
    if num in fib_seq:
        result = f'The number {num} is at index {fib_seq.index(num)}'
    else:
        result = f'The number {num} is not in the sequence'
    
    return result
    