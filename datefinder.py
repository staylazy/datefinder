import cdate
import argparse
import os
import time

if __name__ == '__main__':
    # создаем парсер и даем ему аргумент с директорией 
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, help='finding directory')
    option = parser.parse_args() 
    # вызываем функцию поиска
    t = cdate.DateFinder()
    # ecли нет флага - поиск в текущей 
    if option.dir != None:
        t.date_find(option.dir)
    else:
        t.date_find(os.getcwd())
    print("time: " + time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(t.date)))
    print("filename and path: " + t.file)