import numpy as np
import math


def mod_obrat(a, m):
    a_int = int(a)
    if math.gcd(a_int, m) != 1:
        return None
    return pow(a_int, -1, m)





def mod_obrat_matrix(matrix, mod):      #обратная матрица
    det = int(round(np.linalg.det(matrix)))     #определитель
    det_obr = mod_obrat(det % mod, mod)
    if det_obr is None:
        raise ValueError("Обратная матрица не существует, потому что определитель и модуль не взаимно просты.")

    sopr_matr = np.round(det * np.linalg.inv(matrix)).astype(int) % mod
    return (det_obr * sopr_matr) % mod      #sopr - сопряженная матрица из алг дополнений








def text_to_numbers(text, alph):
    return [alph.index(symbol) for symbol in text if symbol in alph]  # текст в числа

def numbers_to_text(numbers, alph):
    return ''.join(alph[i] for i in numbers)  # числа в текст







def hilla_shifr_recurrent(text, key1, key2, alph):
    text = text.replace(" ", "")    #удаление пробелов
    n = len(key1)       #размер блока
    text = text.ljust((len(text) + n - 1) // n * n, alph[0])  # дополнение до кратной длины, заполнение блока

    text_numbers = text_to_numbers(text, alph)

    shifr_numbers = []
    current_key = key1
    next_key = key2

    for i in range(0, len(text_numbers), n):
        block = np.array(text_numbers[i:i + n]).reshape(n, 1)   # шифрование
        shifr_block = np.dot(current_key, block) % len(alph)
        shifr_numbers.extend(shifr_block.flatten())     #двумерный массив в одномерный


        new_key = np.dot(current_key, next_key) % len(alph)         # обновление ключей
        current_key, next_key = next_key, new_key

    return numbers_to_text(shifr_numbers, alph)             #шифртекст на выходе









def hilla_rashifr_recurrent(text, key1, key2, alph):
    n = len(key1)       #размер блока
    mod = len(alph)
    text_numbers = text_to_numbers(text, alph)  #текст в числа

    keys_used = []      #лист ключей
    current_key = key1.copy()
    next_key = key2.copy()
    num_blocks = (len(text_numbers) + n - 1) // n           #количество блоков текста

    for _ in range(num_blocks):
        keys_used.append(current_key.copy())        #сохранение ключа
        new_key = (current_key @ next_key) % mod  #умножение ключей и обновление
        current_key, next_key = next_key, new_key

    obr_keys = [mod_obrat_matrix(k.astype(int), mod) for k in keys_used]  #обратная матрица для каждого ключа

    rashifr = []
    for i in range(0, len(text_numbers), n):
        block_idx = i // n                                    #индекс блока
        key = obr_keys[block_idx]                                            #соотв ключ
        block = np.array(text_numbers[i:i + n], dtype=int).reshape(n, 1)        #кодировка
        rashifr_block = (key @ block) % mod              #расшифрование
        rashifr.extend(rashifr_block.flatten().tolist())


    original_len = len(text) - (len(text) % n) if len(text) % n != 0 else len(text)
    rashifr = rashifr[:original_len]                         #обрезание до исходной длины

    return numbers_to_text(rashifr, alph)           #числа в текст










def main():
    russian_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    english_alph = "abcdefghijklmnopqrstuvwxyz"

    language = input("Выбери язык (русский или английский): ").strip().lower()
    mode = input("Выбери режим (шифрование или расшифрование): ").strip().lower()
    text = input("Введи текст: ").strip().lower()

    if language in ["русский", "рус"]:
        alph = russian_alph
    elif language in ["английский", "англ"]:
        alph = english_alph
    else:
        print("Неа, попробуй другой язык.")
        return


    size = int(input("Введи размер матрицы (2 или 3): "))
    print(f"Введи первый {size}x{size} ключ построчно через пробелы:")
    key1 = []
    for _ in range(size):
        row = list(map(int, input().split()))
        key1.append(row)
    key1 = np.array(key1)

    print(f"Введи второй {size}x{size} ключ построчно через пробелы:")
    key2 = []
    for _ in range(size):
        row = list(map(int, input().split()))
        key2.append(row)
    key2 = np.array(key2)


    det1 = int(round(np.linalg.det(key1)))              # проверка на НОД определителя и размера алфавита для первого ключа
    nod1 = math.gcd(det1, len(alph))
    if nod1 != 1:
        print(f"Ошибка: НОД определителя первого ключа ({det1}) и размера алфавита ({len(alph)}) равен {nod1}, а должен быть 1.")
        return



    det2 = int(round(np.linalg.det(key2)))          #проверка на НОД определителя и размера алфавита для второго ключа зочзъеювщдгхтцьё
    nod2 = math.gcd(det2, len(alph))
    if nod2 != 1:
        print(f"Ошибка: НОД определителя второго ключа ({det2}) и размера алфавита ({len(alph)}) равен {nod2}, а должен быть 1.")
        return


    if mode in ["шифрование", "шифр"]:
        result = hilla_shifr_recurrent(text, key1, key2, alph)
        print("Зашифрованный текст:", result)
    elif mode in ["расшифрование", "расшифр"]:
        result = hilla_rashifr_recurrent(text, key1, key2, alph)
        print("Расшифрованный текст:", result)
    else:
        print("Ошибка, неправильный режим.")









if __name__ == "__main__":
    main()
