array = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == 'end':
        break

    if command[0] == 'exchange':
        index = int(command[1])

        if index < len(array):
            first_part = array[index:]
            second_part = array[:index]
            print(first_part + second_part)
        else:
            print('Invalid index')

    if command[0] == 'max':

        if command[1] == 'even':
            max_even = -1
            for index, value in enumerate(array):
                if value % 2 == 0 and value > max_even:
                    max_even = index

            if max_even < 0:
                print('No matches')
            else:
                print(max_even)

        if command[1] == 'odd':
            max_odd = -1
            for index, value in enumerate(array):
                if value % 2 != 0 and value > max_odd:
                    max_odd = index

            if max_odd < 0:
                print('No matches')
            else:
                print(max_odd)

    if command[0] == 'min':

        if command[1] == 'even':
            min_even = 1001

            for index, value in enumerate(array):
                if value % 2 == 0 and value < min_even:
                    min_even = index

            if min_even == 1001:
                print('No matches')
            else:
                print(min_even)

        if command[1] == 'odd':
            min_odd = 1001

            for index, value in enumerate(array):
                if value % 2 != 0 and value < min_odd:
                    min_odd = index

            if min_odd == 1001:
                print('No matches')
            else:
                print(min_odd)

    if command[0] == 'first' and command[2] == 'even':
        first_even = []
        counts = int(command[1])

        for count in range(counts):
            for elem in array:
                if elem % 2 == 0:
                    first_even.append(elem)
                    break

        print(first_even)

    if command[0] == 'first' and command[2] == 'odd':
        first_odd = []
        counts = int(command[1])

        for count in range(counts):
            for elem in array:
                if elem % 2 != 0:
                    first_odd.append(elem)
                    break

        print(first_odd)

    if command[0] == 'last' and command[2] == 'even':
        last_even = []

        counts = int(command[1])

        for count in range(counts):
            for elem in array[::-1]:
                if elem % 2 == 0:
                    last_even.append(elem)
                    break

        if len(array) < counts:
            print('Invalid count')
        else:
            print(last_even[::-1])

    if command[0] == 'last' and command[2] == 'odd':
        last_odd = []

        counts = int(command[1])

        for count in range(counts):
            for elem in array[::-1]:
                if elem % 2 != 0:
                    last_odd.append(elem)
                    break

        if len(array) < counts:
            print('Invalid count')
        else:
            print(last_odd[::-1])


print(array)
