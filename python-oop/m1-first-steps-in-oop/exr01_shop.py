class Shop:
    def __init__(self, name: str, items: list) -> None:
        self.name = name
        self.items = items

    def get_items_count(self):
        return len([x for x in self.items])


if __name__ == '__main__':
    shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
    print(shop.get_items_count())
