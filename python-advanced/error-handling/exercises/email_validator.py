class MustContainAtSymbolError(Exception):
    pass


class TooManyAtSymbolsError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainNameError(Exception):
    pass


def validate_email(email):
    """
    """
    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')
        
    username, domain, *rest = email.split('@')

    if len(rest) > 0:
        raise TooManyAtSymbolsError('the whole email must contain one and only one "@" symbol')
    
    if len(username) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    if domain.split('.')[-1] not in ['.com', '.bg', '.net', '.org']:
        raise InvalidDomainNameError('Domain must be one of the following: .com, .bg, .org, .net')


def main():
    """
    """
    while True:
        email = input()
        if email == 'End':
            break
        
        validate_email(email)


if __name__ == '__main__':
    main()
