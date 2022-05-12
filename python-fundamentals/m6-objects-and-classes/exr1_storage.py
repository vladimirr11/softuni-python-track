class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        self.product = product
        if len(self.storage) < self.capacity:
            self.storage.append(self.product)

    def get_products(self):
        return self.storage


if __name__ == '__main__':
    storage = Storage(4)

    storage.add_product('apple')
    storage.add_product('bannana')
    storage.add_product('potato')
    storage.add_product('tomato')
    storage.add_product('bread')

    print(storage.get_products())
