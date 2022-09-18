from project.technology.technology import Technology


class Laptop(Technology):
    def __init__(self, memory: float, memory_taken: float) -> None:
        super().__init__(memory, memory_taken)

    def install_software(self, software, software_memory):
        try:
            memory_left = self.get_capacity(self.memory, software_memory + self.memory_taken)
            self.memory_taken += software_memory
            return memory_left
        except Exception:
            return f'You don\'t have enough space for {software}!'
