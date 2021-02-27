film_name = input()

student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while film_name != 'Finish':
    available_seats = int(input())
    total_tickets = 0
    while total_tickets < available_seats:
        type_ticket = input()
        if type_ticket == 'student':
            total_tickets += 1
            student_tickets += 1
        elif type_ticket == 'standard':
            total_tickets += 1
            standard_tickets += 1
        elif type_ticket == 'kid':
            total_tickets += 1
            kids_tickets += 1
        elif type_ticket == 'End':
            break
    occupied_cinema = (total_tickets / available_seats) * 100
    print(f'{film_name} - {occupied_cinema:.2f}% full.')

    film_name = input()

total_tickets = student_tickets + standard_tickets + kids_tickets
print(f'Total tickets: {total_tickets}')
print(f'{((student_tickets / total_tickets) * 100):.2f}% student tickets.')
print(f'{((standard_tickets / total_tickets) * 100):.2f}% standard tickets.')
print(f'{((kids_tickets / total_tickets) * 100):.2f}% kids tickets.')