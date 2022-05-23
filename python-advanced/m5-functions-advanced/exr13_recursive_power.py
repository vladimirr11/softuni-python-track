def recursive_power(number, power, curr_power=0, curr_result=1, lst=[]):
    curr_result *= number
    lst.append(curr_result)

    curr_power += 1
    if curr_power == power:
        return lst
    else:
        return recursive_power(number, power, curr_power, curr_result, lst)


print(recursive_power(2, 10))
