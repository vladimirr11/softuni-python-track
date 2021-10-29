def multiply(*nums):
    """
    """
    numbers = [int(num) for num in nums]
    
    result = 1
    for i in range(len(numbers)):
        result *= numbers[i]
    
    return result


print(multiply(1, 4, 5))
