class EncryptionGenerator:

    MAX_CHAR_VALUE = 127
    MIN_CHAR_VALUE = 32

    def __init__(self, text) -> None:
        self.text = str(text)

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError('You must add a number.')

        encrypted_chars = []
        for ch in self.text:
            encrypted_ch = ord(ch) + other
            if encrypted_ch > __class__.MAX_CHAR_VALUE:
                encrypted_ch = __class__.MIN_CHAR_VALUE + (encrypted_ch - __class__.MAX_CHAR_VALUE)
            elif encrypted_ch < __class__.MIN_CHAR_VALUE:
                encrypted_ch = __class__.MAX_CHAR_VALUE - (__class__.MIN_CHAR_VALUE - encrypted_ch)
            encrypted_chars.append(chr(encrypted_ch))
        
        return ''.join([ch for ch in encrypted_chars])


if __name__ == '__main__':
    example = EncryptionGenerator('Super-Secret Message')

    print(example + 20)
    print(example + (-52))
