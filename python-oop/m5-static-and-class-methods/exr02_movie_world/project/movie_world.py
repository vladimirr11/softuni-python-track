import sys, os
sys.path.insert(0, os.getcwd())

from exr02_movie_world.project.customer import Customer
from exr02_movie_world.project.dvd import DVD


class MovieWorld:

    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name) -> None:
        self.name = name
        self.customers = list()
        self.dvds = list()

    @staticmethod
    def dvd_capacity() -> int:
        return __class__.DVD_CAPACITY
    
    @staticmethod
    def customer_capacity() -> int:
        return __class__.CUSTOMER_CAPACITY
    
    def add_customer(self, customer: Customer) -> bool:
        if len(self.customers) + 1 <= self.customer_capacity():
            self.customers.append(customer)
    
    def add_dvd(self, dvd: DVD) -> bool:
        if len(self.dvds) + 1 <= self.dvd_capacity():
            self.dvds.append(dvd)
        
    def rent_dvd(self, customer_id, dvd_id) -> str:
        customer: Customer = [customer for customer in self.customers if customer.id == customer_id][0]
        dvd: DVD = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        
        if dvd.id in [dvd.id for dvd in customer.rented_dvds]:
            return f'{customer.name} has already rented {dvd.name}'
        
        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'
        
        if dvd.is_rented:
            return 'DVD is already rented'
        
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True

        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id) -> str:
        customer: Customer = list(filter(lambda c: c.id == customer_id, self.customers))[0]

        if dvd_id in [dvd.id for dvd in customer.rented_dvds]:
            dvd: DVD = list(filter(lambda dvd: dvd.id == dvd_id, self.dvds))[0]

            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)

            return f'{customer.name} has successfully returned {dvd.name}'
        
        return f'{customer.name} does not have that DVD'

    def __repr__(self) -> str:
        customers = '\n'.join([customer.__repr__() for customer in self.customers])
        dvds = '\n'.join([dvd.__repr__() for dvd in self.dvds])

        message = ''
        message += customers + '\n'
        message += dvds

        return message


if __name__ == '__main__':
    c1 = Customer('John', 16, 1)
    c2 = Customer('Anna', 55, 2)

    d1 = DVD('Black Widow', 1, 2020, 'April', 18)
    d2 = DVD.from_date(2, 'The Croods 2', '23.12.2020', 3)

    movie_world = MovieWorld('The Best Movie Shop')

    movie_world.add_customer(c1)
    movie_world.add_customer(c2)

    movie_world.add_dvd(d1)
    movie_world.add_dvd(d2)

    print(movie_world.rent_dvd(1, 1))
    print(movie_world.rent_dvd(2, 1))
    print(movie_world.rent_dvd(1, 2))

    print(movie_world)
