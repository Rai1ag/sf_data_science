"""Игра "Угадай число"!"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

count = 0 # счётчки кол-ва попыток

while True: # цикл, позволяющий вводить и угадывать числа
    count += 1
    predict_number = int(input('Угадай число от 1 до 100!'))
    
    if predict_number > number:
        print('Число должно быть меньше!')
        
    elif predict_number < number:
        print('Число должно быть больше!')
        
    else:
        print(f'Вы угадали число! Это число = {number}, за {count} попыток.')
        break # Выход из цикла (конец игры)