from collections import deque


def best_list_pureness(numbers_list: list, k: int):
    """
    """
    pureness_list = []

    numbers_deque = deque(numbers_list)
    for _ in range(k + 1):
        curr_pureness = 0    
        for (idx, num) in enumerate(numbers_deque):
            curr_pureness += idx * num

        last_el = numbers_deque.pop()
        numbers_deque.appendleft(last_el)

        pureness_list.append(curr_pureness)

    max_pureness_value = -2934749349
    pureness_idx = 0

    for (idx, value) in enumerate(pureness_list):
        if value > max_pureness_value:
            max_pureness_value = value
            pureness_idx = idx

    return f'Best pureness {max_pureness_value} after {pureness_idx} rotations'


if __name__ == '__main__':
    test = ([4, 3, 2, 6], 4)
    result = best_list_pureness(*test)

    print(result)
