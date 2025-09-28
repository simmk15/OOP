class dog:
    species="animal"
    def __init__(self,breed,colour):
        self.breed=breed
        self.colour=colour
tommy=dog("Golden retriever","Golden")
polo=dog("Husky","White")
print("Tommy is a",tommy.species)
print("Polo is also a",polo.species)
print("The breed is=",tommy.breed, "\nColour is=",tommy.colour)
print("The breed is=",polo.breed,"\nColour is=",polo.colour)