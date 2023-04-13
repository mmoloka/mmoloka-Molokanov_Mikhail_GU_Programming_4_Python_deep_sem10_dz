import json
import os

# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа
# (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

class User:
    ids = set()
    accesses = set(range(1, 8))
    access_dict = {}


    def __init__(self, name, id, access):
        self.name = name
        self.id = id
        self.access = access

    def get_user(self):
        while True:
            self.name = input('Введите имя: ')
            if self.name == '':
                break
            self.id = int(input('Введите личный идентификатор: '))
            while self.id in self.ids:
                print('Пользователь с таким идентификатором уже существует!')
                self.id = int(input('Введите личный идентификатор: '))
            else:
                self.ids.add(self.id)        
            self.access = int(input('Введите уровень доступа от 1 до 7: '))
            while self.access not in self.accesses:
                print('Такого уровня доступа не существует!')
                self.access = int(input('Введите уровень доступа от 1 до 7: '))

            self.access_dict.setdefault(self.access, {})[self.id] = self.name
    
    def log_user(self, json_file):
        for obj in os.listdir():
            if os.path.isfile(obj) and obj == json_file:
                with open(json_file, 'r', encoding='utf-8') as f:
                    self.access_dict = json.load(f)

        for _, value in self.access_dict.items():
            for id, _ in value.items():
                self.ids.add(int(id))

            with open(json_file, 'w', encoding='utf-8') as j:
                json.dump(self.access_dict, j, ensure_ascii=False)    


if __name__ == '__main__':
    u = User(None, None, None)
    u.get_user()
    u.log_user('log_access.json')