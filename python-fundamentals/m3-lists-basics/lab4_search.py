num = int(input())
searched_word = input()

list_of_strings = []
filtered_list = []

for _ in range(num):
    string = input()
    list_of_strings.append(string)
    if searched_word in string:
        filtered_list.append(string)

print(list_of_strings)
print(filtered_list)
