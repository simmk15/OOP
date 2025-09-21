class india():
    def capital(self):
        print("New delhi is the capital of india")
    def language(self):
        print("Hindi is the most widely spoken language of india")
    def type(self):
        print("India is a developing country")
class usa():
    def capital(self):
        print("Washington D.C is the capital of USA")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA id a developed country")
obj_india=india()
obj_usa=usa()
for country in(obj_india,obj_usa):
    country.capital()
    country.language()
    country.type()