class Cat:
    name: str
    age: int
    breed: str
    gender: str

    def __init__(self, name, age, breed, gender):
        self.name = name
        self.age = age
        self.breed = breed
        self.gender = gender

    def __repr__(self):
        return f"Имя: {self.name}"

    def meow(self):
        if self.age > 10:
            return "Meow, motherfucker"
        else:
            return "meow"

    def eat(self, food_type):
        return f"{self.name} съела {food_type}"


new_cat = Cat("Мурка", 11, "Сиамская", "мужыыык")
print(new_cat)
user_input = input("Введите еду: ")
print(new_cat.eat(food_type=user_input))
