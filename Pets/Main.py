import csv

from Classes import *


class PetRegistry:
    def __init__(self):
        self.animals = []
        self.counter = Counter()

    def add_new_animal(self, animal):
        self.animals.append(animal)
        self.counter.add()

    def teach_command(self, animal, command):
        animal.set_command(command)

        with open("DataBase.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            animal_type = self.get_animal_type(animal)
            animal_name = animal.name
            writer.writerow([animal_type, animal_name, command])

    @staticmethod
    def get_animal_type(animal):
        if isinstance(animal, Dog):
            return "Собака"
        elif isinstance(animal, Cat):
            return "Кошка"
        elif isinstance(animal, Hamster):
            return "Хомяк"
        elif isinstance(animal, Horse):
            return "Лошадь"
        elif isinstance(animal, Camel):
            return "Верблюд"
        elif isinstance(animal, Donkey):
            return "Осёл"
        return ""

    def get_commands(self, animal):
        return [animal.get_command()]

    def read_database(self):
        try:
            with open("DataBase.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 3:
                        animal_name = row[0]
                        command = row[2]
                        animal = next((a for a in self.animals if a.name == animal_name), None)
                        if animal:
                            animal.set_command(command)
        except FileNotFoundError:
            pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.counter.get_count() == 0:
            raise Exception("Error")
        else:
            self.counter.reset_count()


def main():
    with PetRegistry() as pet_registry:
        while True:
            print("1. Новый питомец")
            print("2. Выучить комманду")
            print("3. Дать команду")
            print("4. Выход")
            choice = int(input())
            if choice == 1:
                print("Тип животного: ")
                animal_type = input()
                print("Дайте имя питомцу: ")
                animal_name = input()
                animal = None
                if animal_type == "Собака":
                    animal = Dog(animal_name)
                elif animal_type == "Кошка":
                    animal = Cat(animal_name)
                elif animal_type == "Хомяк":
                    animal = Hamster(animal_name)
                elif animal_type == "Лошадь":
                    animal = Horse(animal_name)
                elif animal_type == "Верблюд":
                    animal = Camel(animal_name)
                elif animal_type == "Осёл":
                    animal = Donkey(animal_name)
                else:
                    raise ValueError("Такого вида животных у нас нет: " + animal_type)
                pet_registry.add_new_animal(animal)
            elif choice == 2:
                print("Имя питомца: ")
                animal_name = input()
                found_animal = next((a for a in pet_registry.animals if a.name == animal_name), None)
                if found_animal is None:
                    print("Нет такого животного")
                    continue
                print("Введите команду: ")
                command = input()
                pet_registry.teach_command(found_animal, command)
            elif choice == 3:
                print("Имя питомца: ")
                animal_name = input()
                found_animal = next((a for a in pet_registry.animals if a.name == animal_name), None)
                if found_animal is None:
                    print("Нет такого животного")
                    continue
                commands = pet_registry.get_commands(found_animal)
                for cmd in commands:
                    print(cmd)
            elif choice == 4:
                return
            


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
