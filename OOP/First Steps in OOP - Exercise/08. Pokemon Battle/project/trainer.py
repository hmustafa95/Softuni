from pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name):
        try:
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        except:
            return 'Pokemon is not caught'

        self.pokemons.remove(pokemon)

        return f'You have released {pokemon_name}'

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\n'
        result += f'Pokemon count {len(self.pokemons)}\n'
        for idx in self.pokemons:
            result += f'- {idx.pokemon_details()}\n'
        return result
