N = int(input())

odd_numbers_set = set()
even_numbers_set = set()

for idx in range(N):
    name = input()
    ord_sum = sum([ord(ch) for ch in name])
    number = ord_sum // (idx + 1)
    if number % 2 == 0:
        even_numbers_set.add(number)
    else:
        odd_numbers_set.add(number)


if sum(odd_numbers_set) == sum(even_numbers_set):
    union = odd_numbers_set.union(even_numbers_set)
    print(', '.join(map(str, list(union))))
elif sum(odd_numbers_set) > sum(even_numbers_set):
    difference = odd_numbers_set.difference(even_numbers_set)
    print(', '.join(map(str, list(difference))))
elif sum(odd_numbers_set) < sum(even_numbers_set):
    symetric_difference = odd_numbers_set.symmetric_difference(even_numbers_set)
    print(', '.join(map(str, list(symetric_difference))))
