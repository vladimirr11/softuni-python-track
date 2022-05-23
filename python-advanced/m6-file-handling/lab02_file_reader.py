sum_file_nums = 0

with open('./06-File-Handling-Lab-Resources/File Reader/numbers.txt', 'r') as file:
    for line in file:
        sum_file_nums += int(line)

    print(sum_file_nums)
