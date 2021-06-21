from collections import deque


def rotate_hot_potato(people, tosses_count):
    """
    """
    people = deque(people)

    index = 0

    while True:
        if len(people) == 1:
            print(f'Last is {people[0]}')
            break

        index += 1

        person = people.popleft()
        if index == tosses_count:
            print(f'Removed {person}')
            index = 0
        else:
            people.append(person)


rotate_hot_potato(input().split(), int(input()))
