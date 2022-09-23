def get_primes(numbers):

    list_of_primes = list()

    def check_is_number_prime(number):
        for i in range(2, number):
            if number % i == 0:
                return False

        return True

    for n in numbers:
        if n < 2:
            continue
        
        is_prime = check_is_number_prime(n)
        if is_prime:
            list_of_primes.append(n)
    
    for prime in list_of_primes:
        yield prime


if __name__ == '__main__':
    print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
