from collections import deque


working_bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))

symbols = deque(input().split())


def calculate_honey(bee_value, nectar_value, symbol):
    if symbol == '+':
        return abs(bee_value + nectar_value)
    elif symbol == '-':
        return abs(bee_value - nectar_value)
    elif symbol == '*':
        return abs(bee_value * nectar_value)
    elif symbol == '/':
        if nectar_value == 0:
            return 0
        return abs(bee_value / nectar_value)


total_honey_made = 0
while len(working_bees) > 0 and len(nectar) > 0:
    curr_bee_value = working_bees.popleft()
    curr_nectar_value = nectar.pop()

    if curr_bee_value > curr_nectar_value:
        working_bees.appendleft(curr_bee_value)
        del curr_nectar_value
        if len(nectar) == 0:
            break

        continue

    curr_symbol = symbols.popleft()

    total_honey_made += calculate_honey(curr_bee_value,
                                        curr_nectar_value, curr_symbol)

    del curr_bee_value
    del curr_nectar_value
    del curr_symbol


print(f'Total honey made: {total_honey_made}')
if working_bees:
    print(f'Bees left: {", ".join([str(bee) for bee in working_bees])}')
if nectar:
    print(f'Nectar left: {", ".join([str(n) for n in nectar])}')
