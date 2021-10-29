import math


class Integer:
    def __init__(self, value) -> None:
        self.value = value

    @classmethod
    def from_float(cls, value):
        if isinstance(value, float):
            return cls(math.floor(value))
        
        return 'value is not a float'

    @classmethod
    def from_roman(cls, value):
        roman = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000,
                'IV': 4,
                'IX': 9,
                'XL': 40,
                'XC': 90,
                'CD': 400,
                'CM': 900}

        i = 0
        number = 0
        while i < len(value):
            if i + 1 < len(value) and value[i: i + 2] in roman:
                number += roman[value[i: i + 2]]
                i += 2
            else:
                number += roman[value[i]]
                i += 1

        return cls(number)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            return cls(int(value))
        
        return 'wrong type'


if __name__ == '__main__':
    first_num = Integer(10)
    second_num = Integer.from_roman('IV')
    print(Integer.from_float('2.6'))
    print(Integer.from_string(2.6))
