numbers: str = input().split()

result = [number for number in sorted(numbers, reverse=True)]

print(''.join(result))
