

class auto:
    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.clor = color
        self.mark = mark
        self.weight = weight

    def move(self):
        return "move"

    def stop(self):
        return "stop"

    def birthday(self):
        return self.age + 1

car1 = auto('Audi', 4, 'red', 'A6', '2 t')
print(car1.brand, car1.age, car1.mark, car1.birthday())
