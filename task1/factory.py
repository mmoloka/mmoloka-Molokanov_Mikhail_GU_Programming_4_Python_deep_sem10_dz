from heirs import*

# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Factory:

    def __init__(self, animal_type, name, area, feature):
        self.animal_type = animal_type
        self.name = name
        self.area = area
        self.feature =feature

    def get_animal_class(self):
        if self.animal_type == 'fish':
            return Fish(self.name, self.area, self.feature)
        elif self.animal_type == 'bird':
            return Bird(self.name, self.area, self.feature)
        elif self.animal_type == 'reptile':
            return Reptile(self.name, self.area, self.feature)  


if __name__ == '__main__':
    f = Factory('fish', 'trout', 'lake', 100)
    b = Factory('bird', 'falcon', 'field', 0.5)
    r = Factory('reptile', 'crocodile', 'river', 3.5)
    
    print(f'{f.get_animal_class().name} lives in {f.get_animal_class().area}\
 on max depth {f.get_animal_class().get_max_depth()} m')
    print(f'{b.get_animal_class().name} lives in {b.get_animal_class().area},\
 have wing length {b.get_animal_class().get_wing_length()} m')
    print(f'{r.get_animal_class().name} lives in {r.get_animal_class().area},\
 have body length {r.get_animal_class().get_body_length()} m')          