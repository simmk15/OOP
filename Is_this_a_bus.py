class vehicle:
    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage
class bus(vehicle):
    pass
school_bus=bus("School Volvo",180,12)
print("Vehicle name-",school_bus.name,"Speed-",school_bus.max_speed,"milage-",school_bus.milage)