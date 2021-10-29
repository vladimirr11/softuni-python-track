class Profile:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError('The username must be between 5 and 15 characters.')
        
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.is_password_required_length(value) \
            and self.is_password_contain_uppercase_letter(value) \
            and self.is_password_contain_digit(value):

    	    self.__password = value
        else:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')        

    def is_password_required_length(self, password):
        return len(password) >= 8
    
    def is_password_contain_uppercase_letter(self, password):
        uppercase_letters = [ch for ch in password if ch.isupper()]
    
        return True if uppercase_letters else False

    def is_password_contain_digit(self, password):
        digits = [ch for ch in password if ch.isdigit()]

        return True if digits else False

    def __str__(self) -> str:
        return f'You have a profile with username: \"{self.__username}\" and password: {"*" * len(self.__password)}'


if __name__ == '__main__':
    # profile_with_invalid_password = Profile('My_username', 'My-password')

    # profile_with_invalid_username = Profile('Too_long_username', 'Any')

    correct_profile = Profile('Username','Passw0rd')
    print(correct_profile)
