password = input()


def check_len_password(password: str):
    if len(password) < 6 or len(password) > 10:
        return 'Password must be between 6 and 10 characters'


def is_password_alpha_or_digit(password: str):
    for char in password:
        if not char.isalpha() and not char.isdigit():
            return 'Password must consist only of letters and digits'


def is_password_contain_two_digits(password: str):
    counter = 0
    for char in password:
        if char.isdigit():
            counter += 1
    if counter < 2:
        return 'Password must have at least 2 digits'


def password_validator(password: str):
    validators = [
        check_len_password,
        is_password_alpha_or_digit,
        is_password_contain_two_digits
    ]

    validation_errors = []

    for validator in validators:
        result = validator(password)
        if result is not None:
            validation_errors.append(result)

    if len(validation_errors) == 0:
        return 'Password is valid'
    else:
        return '\n'.join(validation_errors)


print(password_validator(password))
