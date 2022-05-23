def palindrome(word, indx):
    if len(word) // 2 == indx:
            return f'{word} is a palindrome'
    if word[indx] != word[len(word) - 1 - indx]:
        return f'{word} is not a palindrome'
        
    return palindrome(word, indx + 1)
    

print(palindrome('abcba', 0))
print(palindrome('peter', 0))
