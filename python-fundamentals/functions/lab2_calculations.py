operator = input()
int_one = int(input())
int_two = int(input())

def calculate(int_one, int_two, operator):
    result = None

    if operator == 'multiply':
        result = int_one * int_two
    if operator == 'divide':
        result = int(int_one / int_two)
    if operator == 'add':
        result = int_one + int_two
    if operator == 'subtract':
        result = int_one - int_two
    
    return result


print(calculate(int_one, int_two, operator))
