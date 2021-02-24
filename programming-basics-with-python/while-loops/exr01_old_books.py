book_name = input()
books_count = int(input())

counter = 0
is_book_found = False

while counter < books_count:
    current_book = input()

    if current_book == book_name:
        is_book_found = True
        print(f'You checked {counter} books and found it.')
        break

    counter += 1

if not is_book_found:
    print(f'The book you search is not here!')
    print(f'You checked {books_count} books. ')