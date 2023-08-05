import random


    # Читаем все строки из файла
with open('agents.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Выбираем случайную строку
random_string = random.choice(lines) 
print(random_string)
