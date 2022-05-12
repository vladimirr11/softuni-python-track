def get_grade(grade):
    if 2.0 <= grade <= 2.99:
        return 'Fail'
    if 3.0 <= grade <= 3.49:
        return 'Poor'
    if 3.5 <= grade <= 4.49:
        return 'Good'
    if 4.5 <= grade <= 5.49:
        return 'Very Good'
    if 5.5 <= grade <= 6.0:
        return 'Excellent'


score = float(input())
print(get_grade(score))
