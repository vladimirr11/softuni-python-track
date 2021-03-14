electrons = int(input())

my_list = []

for e_shell in range(1, 9):
    current_shell = 2 * e_shell ** 2
    if current_shell <= electrons:
        my_list.append(current_shell)
    electrons -= current_shell
    if current_shell > electrons and electrons > 0:
        my_list.append(electrons)
    if current_shell < electrons and electrons < 2 * (e_shell + 1) ** 2:
        my_list.append(electrons)


print(my_list)