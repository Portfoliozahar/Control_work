class Animal:
    def __init__(self, name):
        self.name = name
        self.command = None

    def set_command(self, command):
        self.command = command

    def get_command(self):
        return self.command


class PackAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)


class Pet(Animal):
    def __init__(self, name):
        super().__init__(name)


class Camel(PackAnimal):
    def __init__(self, name):
        super().__init__(name)


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)


class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)


class Donkey(PackAnimal):
    def __init__(self, name):
        super().__init__(name)


class Hamster(Pet):
    def __init__(self, name):
        super().__init__(name)


class Horse(PackAnimal):
    def __init__(self, name):
        super().__init__(name)


class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def get_count(self):
        return self.count

    def reset_count(self):
        self.count = 0    
