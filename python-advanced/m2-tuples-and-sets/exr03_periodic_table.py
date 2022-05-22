def print_unique_chemicals(num):
    chemicals = set()

    for _ in range(num):
        chems = input().split()
        for chem in chems:
            chemicals.add(chem)
    
    [print(chem) for chem in chemicals]


print_unique_chemicals(int(input()))
