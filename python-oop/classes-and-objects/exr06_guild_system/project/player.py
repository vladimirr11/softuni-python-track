class Player:
    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'
    
    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return f'Skill already added'
        
        self.skills[skill_name] = mana_cost
        return f'Skill {skill_name} added to the collection of the player {self.name}'
    
    def player_info(self):
        message = f'Name: {self.name}\n'
        message += f'Guild: {self.guild}\n'
        message += f'HP: {self.hp}\n'
        message += f'MP: {self.mp}\n'
        for (k, v) in self.skills.items():
            message += f'==={k} - {v}\n'
        
        return message
        