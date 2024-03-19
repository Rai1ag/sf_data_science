"""Игра "Угадай число". Компьютер сам загадывает и угадавыет число."""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадавыем число.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток.
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        
        if number == predict_number:
            break
    return(count)

# print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int: #
    """Среднее значение попыток угадывания нашего алгоритма за 1000 подходов.

    Args:
        random_predict ([type]): Функция угадывания.

    Returns:
        int: Среднее количество попыток.
    """
    
    count_ls = [] # список для сохранения кол-ва попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # среднее кол-во попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__': # специальная констуркция, чтобы отделить "вызов кода" от "импорта"
    score_game(random_predict) # запускаем