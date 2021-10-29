class ValueCannotBeNegative(Exception):
    def __init__(self, value):
        message = f'Value {value} is negative!'
        super(ValueCannotBeNegative, self).__init__(message)


while True:
    positive_number = int(input())
    if positive_number <= 0:
        raise ValueCannotBeNegative(positive_number)
        