num = input()

prime_num = 0
non_prime_num = 0

while num != 'stop':
    num = int(num)
    if num < 0:
        print(f'Number is negative.')
    else:
        for i in range(2, num):
            if num % i == 0:
                non_prime_num += num
                break
        else:
            prime_num += num

    num = input()

print(f'Sum of all prime numbers is: {prime_num}')
print(f'Sum of all non prime numbers is: {non_prime_num}')
