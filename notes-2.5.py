# create a class that represents a pokemon
# class Pokemon: # always name classes with capital
#     def __init__(self):
#         """Constructor:contains all properties of a Pokemon. It also contains the default state of the properties."""
        
#         self.name = ""
#         self.id = 0
#         self.weight = 0
#         self.height = 0
#         self.type = "Normal"
#         self.actual_cry = "Rooooooooar"

#     def cry(self) -> str:
#         """Represents the sound a pokemon makes
        
#         Returns:
#             - As a string the sound a pokemon makes"""
#         return f"{self.name} says, \"{self.actual_cry}!\""
    
#     def consume(self , item: str) -> str:
#         """Pokemon consumes the item
        
#         Params:
#             - the item the pokemon consumes

#         Returns:
#             - the response of the pokemon
#         """
#         if item.lower() == "berry":
#             return f"{self .name} eats the berry and says, \"YUM!\""
#         elif item.lower() == "potion":
#             return f"{self.name} feels much better after the potion!"
#         else: return f"{self.name} batted away the {item}!"


# def main():
#     # create two Pokemon

#     # create something 'Pikachu'-like
#     pokemon_one = Pokemon()
#     # access the properties inside pokemon_one
#     # print the name of pokemon_one
#     print(pokemon_one.name)
#     print(pokemon_one.type)

#     # change the values of the properties
#     pokemon_one.name = "Pikachu"
#     pokemon_one.type = "Electric"
#     pokemon_one.id = 25

#     # print the values from pokemon_one
#     print(pokemon_one.name)
#     print(pokemon_one.type)
    


#      # create something 'Squirtle'-like
# def main():
#     pokemon_two = Pokemon()
#     print(pokemon_two.name)
#     print(pokemon_two.type)
#     pokemon_two.name = "Squirtle"
#     pokemon_two.type = "Water"
#     pokemon_two.id = 26

#     # test pokemon cry
#     print(pokemon_two.cry())

# if __name__ == "__main__":
#     main()

#     pass

class Hoopa(Pokemon):
    def __init__(self,name="Hoopa"):
        super().__init__()
        self.name = name
        self.id = 720
        self.type = "Psychic","Ghost"
        self.actual_cry = "Hoopa!"

    def shadow_ball(self, defender: Pokemon) -> str:
        response = f"{self.name} used shadow ball on {defender.name}."
        if defender.type.lower() == "dark":
           response = response + " It was super effective."
        return response