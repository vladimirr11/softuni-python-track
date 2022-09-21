def start_playing(cls):
    return cls.play()


if __name__ == '__main__':
    class Guitar:
        def play(self):
            return 'Playing the guitar'

    guitar = Guitar()
    start_playing(guitar)
