N = int(input())

intersections_list = []

for i in range(N):
    (range_one, range_two) = input().split('-')
    (start_one, end_one), (start_two, end_two) = range_one.split(','), range_two.split(',')

    set_one = {i for i in range(int(start_one), int(end_one) + 1)}
    set_two = {i for i in range(int(start_two), int(end_two) + 1)}

    intersec = set_one.intersection(set_two)

    intersections_list.append(intersec)


def find_longest_intersection(intersec_list: list):
    max_length = 0
    idx_max_length = 0
    for idx, sett in enumerate(intersec_list):
        if len(sett) > max_length:
            max_length = len(sett)
            idx_max_length = idx

    return intersec_list[idx_max_length]


longest_intersec = list(find_longest_intersection(intersections_list))

print(f'Longest intersection is [{", ".join(map(str, longest_intersec))}] \
with length {len(longest_intersec)}')
