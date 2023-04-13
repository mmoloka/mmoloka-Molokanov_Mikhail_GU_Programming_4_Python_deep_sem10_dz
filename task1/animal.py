class Animal:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'{self.name} lives in {self.area}'


if __name__ == '__main__':
    a = Animal('monkey', 'jungle')
    print(a)        