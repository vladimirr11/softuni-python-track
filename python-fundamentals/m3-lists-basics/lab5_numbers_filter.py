num = int(input())

number_container = [int(input()) for number in range(num)]

command = input()

filtered_container = []

for number in number_container:
    if command == 'even' and number % 2 == 0:
        filtered_container.append(number)
    elif command == 'odd' and number % 2 == 1:
        filtered_container.append(number)
    elif command == 'positive' and number >= 0:
        filtered_container.append(number)
    elif command == 'negative' and number < 0:
        filtered_container.append(number)

print(filtered_container)
