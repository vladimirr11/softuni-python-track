class Time:

    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f'{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}' 

    def next_second(self):
        if Time.max_seconds > self.seconds:
            self.seconds += 1
            return self.get_time()
        elif Time.max_seconds == self.seconds and Time.max_minutes > self.minutes:
            self.seconds = 0
            self.minutes += 1
            return self.get_time()
        elif Time.max_seconds == self.seconds and Time.max_minutes == self.max_minutes and Time.max_hours > self.hours:
            self.seconds = 0
            self.minutes = 0
            self.hours += 1
            return self.get_time()
        elif Time.max_seconds == self.seconds and Time.max_minutes == self.max_minutes and Time.max_hours == self.hours:
            self.seconds = 0
            self.minutes = 0
            self.hours = 0
            return self.get_time()


time = Time(9, 30, 58)

print(time.get_time())
print(time.next_second())

time = Time(10, 59, 59)

print(time.next_second())

time = Time(23, 59, 59)

print(time.next_second())
