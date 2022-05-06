import sys

num = int(input())

min_value = sys.maxsize
counter = 0

while counter < num:
    new_entry = int(input())
    counter += 1
    if new_entry < min_value:
        min_value = new_entry

print(min_value)
