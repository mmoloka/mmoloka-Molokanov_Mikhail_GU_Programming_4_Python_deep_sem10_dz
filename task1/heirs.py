from animal import* 


class Fish(Animal):

    def __init__(self, name, area, max_depth):
        super().__init__(name, area)
        self.max_depth = max_depth

    def get_max_depth(self):
        return self.max_depth


class Bird(Animal):
    def __init__(self, name, area, wing_length):
        super().__init__(name, area)
        self.wing_length = wing_length

    def get_wing_length(self):
            return self.wing_length


class Reptile(Animal):

    def __init__(self, name, area, body_length):
        super().__init__(name, area)
        self.body_length = body_length

    def get_body_length(self):
        return self.body_length


if __name__ == '__main__':
    f = Fish('trout', 'lake', 100)
    b = Bird('falcon', 'field', 0.5)
    r = Reptile('crocodile', 'river', 3.5)

    print(f'{f.name} lives in {f.area} on max depth {f.get_max_depth()} m')
    print(f'{b.name} lives in {b.area}, have wing length {b.get_wing_length()} m')
    print(f'{r.name} lives in {r.area}, have body length {r.get_body_length()} m')