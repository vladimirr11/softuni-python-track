cards = input().split()
num_shuffles = int(input())

middle_index = len(cards) // 2

for shuffle in range(num_shuffles):
    result = []
    for i in range(middle_index):
        first_card = cards[i]
        second_card = cards[i + middle_index]
        result.append(first_card)
        result.append(second_card)

    cards = result

print(cards)
