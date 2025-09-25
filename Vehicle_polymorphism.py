class bmw():
    def fuel_type(self):
        print("Premium gas")
    def max_speed(self):
        print("200 mph")
class ferrari():
    def fuel_type(self):
        print("Premium fuel")
    def max_speed(self):
        print("210 mph")
obj_bmw=bmw()
obj_ferrari=ferrari()
for car in(obj_bmw,obj_ferrari):
    car.fuel_type()
    car.max_speed()