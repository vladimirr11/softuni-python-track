input_string = input()
searched_palindrome = input()

my_list_of_palindromes = [element for element in ''.join(input_string).split(' ') \
             if element == ''.join(reversed(element))]

counts_of_searched_palindrome = my_list_of_palindromes.count(searched_palindrome)

print(my_list_of_palindromes)
print(f'Found palindrome {counts_of_searched_palindrome} times')


# def is_palindrome(word):
#     return word == word[::-1]
#
# lambda word: word == word[::-1]