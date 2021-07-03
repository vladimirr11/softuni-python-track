box = list(map(int, input().split()))
rack_capaicty = int(input())

number_racks = 1
current_rack_weight = 0


for i in range(len(box)):
    current_cloth = box.pop()
    if current_cloth + current_rack_weight > rack_capaicty:
        number_racks += 1
        current_rack_weight = 0
    current_rack_weight += current_cloth


print(number_racks)
