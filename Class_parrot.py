class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("blu",10)
woo=parrot("woo",15)
print("Blu is a",blu.species)
print("Woo is also a",woo.species)
print("The name is=",blu.name,"age is=",blu.age)
print("The name is=",woo.name,"age is=",woo.age)