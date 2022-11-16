class Vehicle:
    wheels: int
    doors: int

    def __init__(self, wheels, doors):
        self.wheels = wheels
        self.doors = doors

    def make_sound(self):
        print("Vroom")


class Bycicle(Vehicle):
    break_type: str

    def __init__(self, wheels, doors, break_type):
        super().__init__(wheels, doors)
        self.break_type = break_type

    def __repr__(self):
        return f"{self.wheels} {self.break_type}"


new_bycicle = Bycicle(wheels=2, doors=0, break_type="Дисковые тормоза")
new_car = Vehicle(wheels=4, doors=4)

print(new_bycicle)
print(new_car)
