def create_phonebook():
    """
    """
    phonebook = dict()

    num = 0
    while True:
        entry = input()
        if entry.isdigit():
            num = int(entry)
            break

        first_name, phone_number = entry.split('-')
        
        if first_name not in phonebook:
            phonebook[first_name] = phone_number
        else:
            phonebook[first_name] = phone_number

    for i in range(num):
        person = input()
        if person in phonebook:
            print(f'{person} -> {phonebook[person]}')
            del phonebook[person]
        else:
            print(f'Contact {person} does not exist.')
    

create_phonebook()
