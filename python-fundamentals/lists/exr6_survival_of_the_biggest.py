string_of_intigers = list(map(int, input().split()))
count_of_numbers_to_remove = int(input())

MIN_NUMBER = 48564804

for i in range(count_of_numbers_to_remove):
    for j in range(len(string_of_intigers)):
        if string_of_intigers[j] < MIN_NUMBER:
            MIN_NUMBER = string_of_intigers[j]

    string_of_intigers.remove(MIN_NUMBER)

    MIN_NUMBER = 48564804

# for i in range(count_of_numbers_to_remove):
#     string_of_intigers.remove(min(string_of_intigers))

print(string_of_intigers)