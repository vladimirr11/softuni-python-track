import sys
import os
sys.path.insert(0, os.getcwd())

from exr08_pokemon_batle.project.pokemon import Pokemon

class Trainer:
    def __init__(self, name) -> None:
        self.name = name
        self.pokemons = []
    
    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'
        
        return f'This pokemon is already caught'
    
    def release_pokemon(self, pokemon_name: str):
        # pokemon = list(filter(lambda p: p.name == pokemon_name, self.pokemon))
        pokemon = [p for p in self.pokemons if p.name == pokemon_name]
        if pokemon:
            self.pokemons.remove(pokemon[0])
            return f'You have released {pokemon_name}'
        
        return f'Pokemon is not caught'
    
    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n'
        for pok in self.pokemons:
            result += f'- {pok.pokemon_details()}\n'

        return result


pokemon = Pokemon("Pikachu", 90)

print(pokemon.pokemon_details())

trainer = Trainer("Ash")

print(trainer.add_pokemon(pokemon))

second_pokemon = Pokemon("Charizard", 110)

print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
