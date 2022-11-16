human_list = []


def add_human(name: str, age: int, sex: str):
    new_human = [name, age, sex]
    human_list.append(new_human)

# print(human_list)


add_human("Arstan", 19, "female")
add_human("Байас", 16, "male")


human_list[0][2] = "male"
# print(human_list)


class Human:
    name: str
    age: int
    sex: str

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __repr__(self) -> str:
        return f"Human with name {self.name}"


new_human = Human(name="Арстан", age=19, sex="male")

print(new_human)
