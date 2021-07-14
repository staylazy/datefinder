import os
from datefinder import *

class DateFinder():
    def __init__(self):
        self.date = 1000000000000
        self.file = ''
        
    def date_find(self, current_dir):
        # возвращаем все файлы папки 
        files = os.listdir(current_dir)
        # для каждого файла спрашиваем расширение если папка - рекурсивный вызов
        # иначе сравниваем время создания с предыдущим
        for i in files:
            path = os.path.join(current_dir, i)
            print(path)
            if os.path.isdir(path):
                self.date_find(path)
            else:
                new_date = os.path.getmtime(path)
                if new_date < self.date:
                    self.date = new_date
                    self.file = path
        