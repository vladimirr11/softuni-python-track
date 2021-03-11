fst_n = int(input())
scd_n = int(input())


def get_factorial_division(first_number, second_number):
    """
    """
    fn_fact = 1
    for i in range(1, first_number + 1):
        fn_fact *= i
    
    sn_fact = 1
    for i in range(1, second_number + 1):
        sn_fact *= i
    
    result = fn_fact / sn_fact

    return f'{result:.2f}'


print(get_factorial_division(fst_n, scd_n))   