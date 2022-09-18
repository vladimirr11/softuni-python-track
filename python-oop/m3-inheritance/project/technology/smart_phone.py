from project.technology.technology import Technology


class SmartPhone(Technology):
    def __init__(self, memory: float, memory_taken: float) -> None:
        super().__init__(memory, memory_taken)

    def install_app(self, app, app_memory):
        try:
            memory_left = self.get_capacity(self.memory, app_memory + self.memory_taken)
            self.memory_taken += app_memory
            return memory_left
        except Exception:
            return f'You don\'t have enough space for {app}!'
