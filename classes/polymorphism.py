"""
Полиморфизм - (лат. много форменность) свойство объектов
которое им позволяет иметь разный функционал без изме-
нения самого класса
"""
class Adder():
    x: int
    y: int
    z: int
    nums: tuple

    def __init__(self, x = 0, y = 0, z = 0, *nums):
        self.x = x
        self.y = y
        self.z = z
        self.nums = nums

    def add(self):
        return self.x + self.y + self.z + sum(list(self.nums))

new_obj = Adder(1, 2, 3, 4, 5)
new_obj2 = Adder(1, 2)
new_obj3= Adder(1, 2, 3)
new_obj4 = Adder(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(new_obj.add())
print(new_obj2.add())
print(new_obj3.add())
print(new_obj4.add())
