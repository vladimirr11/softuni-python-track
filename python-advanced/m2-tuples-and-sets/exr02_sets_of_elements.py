n, m = list(map(int, input().split()))

set_n = set()
set_m = set()

for _ in range(n):
    set_n.add(int(input()))

for _ in range(m):
    set_m.add(int(input()))


def find_set_intersection(set_n: set, set_m: set):
    return set_n.intersection(set_m)


for set_el in find_set_intersection(set_n, set_m):
    print(set_el)
