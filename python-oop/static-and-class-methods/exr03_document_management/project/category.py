class Category:
    def __init__(self, id, name) -> None:
        self.id = int(id)
        self.name = str(name)
    
    def edit(self, new_name) -> None:
        self.name = new_name
    
    def __repr__(self) -> str:
        return f'Category {self.id}: {self.name}'
        