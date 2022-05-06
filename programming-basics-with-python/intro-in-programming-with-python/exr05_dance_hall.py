import math

length_room = float(input())
width_room = float(input())
wardrobe = float(input())

room_size = length_room * width_room * 10000
size_wardrobe = wardrobe * wardrobe * 10000
bench_size = room_size / 10
available_space = room_size - size_wardrobe - bench_size
num_dancers = available_space / 7040

print(math.floor(num_dancers))
