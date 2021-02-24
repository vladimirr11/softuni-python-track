import sys

num = int(input())

counter = 0
max_value = -sys.maxsize

while counter < num:
    new_entry = int(input())
    counter += 1
    if new_entry > max_value:
        max_value = new_entry

print(max_value)