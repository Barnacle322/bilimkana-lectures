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

    def meow():
        print("Meow, motherfucker")
    
new_cat = Cat("Мурка", 5, "Сиамская", "мужыыык")

new_cat.meow()