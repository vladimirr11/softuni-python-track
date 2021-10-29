from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str) -> None:
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError('Name cannot be empty string or white space!')
        
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type == 'Bread':
            bread = Bread(name, price)
            for food in self.food_menu:
                if food.name == bread.name:
                    raise Exception(f'{food_type} {name} is already in the menu!')

            self.food_menu.append(bread)
            return f'Added {name} ({food_type}) to the food menu'

        elif food_type == 'Cake':
            cake = Cake(name, price)
            for food in self.food_menu:
                if food.name == cake.name:
                    raise Exception(f'{food_type} {name} is already in the menu!')

            self.food_menu.append(cake)
            return f'Added {name} ({food_type}) to the food menu'

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        if drink_type == 'Tea':
            tea = Tea(name, portion, brand)
            for drink in self.drinks_menu:
                if drink.name == tea.name:
                    raise Exception(f'{drink_type} {name} is already in the menu!')

            self.drinks_menu.append(tea)
            return f'Added {name} ({drink_type}) to the drink menu'

        elif drink_type == 'Water':
            water = Water(name, portion, brand)
            for drink in self.drinks_menu:
                if drink.name == water.name:
                    raise Exception(f'{drink_type} {name} is already in the menu!')

            self.drinks_menu.append(water)
            return f'Added {name} ({drink_type}) to the drink menu'

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type == 'InsideTable':
            inside_t = InsideTable(table_number, capacity)
            for table in self.tables_repository:
                if table.table_number == inside_t.table_number:
                    raise Exception(f'Table {table_number} is already in the bakery!')
            
            self.tables_repository.append(inside_t)
            return f'Added table number {table_number} in the bakery'
        
        elif table_type == 'OutsideTable':
            outside_t = OutsideTable(table_number, capacity)
            for table in self.tables_repository:
                if table.table_number == outside_t.table_number:
                    raise Exception(f'Table {table_number} is already in the bakery!')
            
            self.tables_repository.append(outside_t)
            return f'Added table number {table_number} in the bakery'

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and table.is_reserved == False:
                table.is_reserved = True
                return f'Table {table.table_number} has been reserved for {number_of_people} people'
        
        return f'No available table for {number_of_people} people'

    def order_food(self, table_number: int, *food_orders):
        found_table = False
        massage = f''
        available_food = []
        food_not_available = [] 
        for table in self.tables_repository:
            if table.table_number == table_number:
                found_table = True
                for f_order in food_orders:
                    for food in self.food_menu:
                        if f_order == food.name:
                            table.order_food(food)
                            self.total_income += food.price
                            available_food.append(food.__repr__() + '\n')
                    else:
                        food_not_available.append(f_order)
            
        if found_table:
            massage += f'Table {table_number} ordered:\n'
            for food in available_food:
                massage += food
            
            for food in food_not_available:
                massage += food
        else:
            massage = f'Could not find table {table_number}'

        return massage

    def order_drink(self, table_number: int, *drink_orders):
        found_table = False
        massage = f''
        available_drinks = []
        drinks_not_available = [] 
        for table in self.tables_repository:
            if table.table_number == table_number:
                found_table = True
                for d_order in drink_orders:
                    for drink in self.drinks_menu:
                        if d_order == drink.name:
                            table.order_food(drink)
                            self.total_income += drink.price
                            available_drinks.append(drink.__repr__() + '\n')
                    else:
                        drinks_not_available.append(d_order)
            
        if found_table:
            massage += f'Table {table_number} ordered:\n'
            for drink in available_drinks:
                massage += drink
            
            for drink in drinks_not_available:
                massage += drink
        else:
            massage = f'Could not find table {table_number}'

        return massage

    def leave_table(self, table_number: int):
        table_bill = 0
        for table in self.tables_repository:
            if table.table_number == table_number:
                table_bill = table.get_bill()
                table.clear()

        massage = f'Table: {table_number}\n'
        massage += f'Bill: {table_bill:.2f}'

        return massage

    def get_free_tables_info(self):
        massage = f''
        for table in self.tables_repository:
            if table.is_reserved == False:
                massage += table.free_table_info()
        
        return massage

    def get_total_income(self):
        income_massage = f'Total income: {self.total_income:.2f}lv'

        return income_massage
        