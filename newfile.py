class Person:
    def __init__(self, name, age, birth_year, birth_place, hobbies, current_location):
        self.name = name
        self.age = age
        self.birth_year = birth_year
        self.birth_place = birth_place
        self.hobbies = hobbies
        self.current_location = current_location
    
    def introduce(self):
        print(f"Hello! My name is {self.name}.")
        print(f"I am {self.age} years old, and I was born in {self.birth_place} in {self.birth_year}.")
        print(f"My hobbies include {', '.join(self.hobbies)}.")
        print(f"Currently, I live in {self.current_location}.")

# Creating an object of the Person class
wahyu = Person(
    name="Wahyu Prasetya Aji Rofi'i",
    age=20,
    birth_year=2004,
    birth_place="Depok",
    hobbies=["playing badminton", "swimming"],
    current_location="Sukabumi"
)

# Introducing yourself
wahyu.introduce()

