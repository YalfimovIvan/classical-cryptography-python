import numpy as np
import math

def mod_obrat(a, m):
    if math.gcd(a, m) != 1:
        return None  # Обратный элемент не существует
    return pow(a, -1, m)

def mod_obrat_matrix(matrix, mod):      #обратная матрица
    det = int(round(np.linalg.det(matrix)))     #определитель
    det_obr = mod_obrat(det % mod, mod)
    if det_obr is None:
        raise ValueError("Обратная матрица не существует, потому что определитель и модуль не взаимно просты.")

    sopr_matr = np.round(det * np.linalg.inv(matrix)).astype(int) % mod
    return (det_obr * sopr_matr) % mod      #sopr - сопряженная матрица из алг дополнений





def text_to_numbers(text, alph):
    return [alph.index(symbol) for symbol in text if symbol in alph]        #текст в числа

def numbers_to_text(numbers, alph):
    return ''.join(alph[i] for i in numbers)      #числа в текст





def hilla_shifr(text, key, alph):
    text = text.replace(" ", "")        #пробелы
    n = len(key)
    text = text.ljust((len(text) + n - 1) // n * n, alph[0])  # Дополнение до кратной длины для заполнения блока
    text_numbers = text_to_numbers(text, alph)

    shifr_numbers = []
    for i in range(0, len(text_numbers), n):
        block = np.array(text_numbers[i:i + n]).reshape(n, 1) #столбец
        shifr_block = np.dot(key, block) % len(alph)        #умнож матрица на столбец
        shifr_numbers.extend(shifr_block.flatten())

    return numbers_to_text(shifr_numbers, alph)





def hilla_rashifr(text, key, alph):
    key_obr = mod_obrat_matrix(key, len(alph))
    text = text.replace(" ", "")
    n = len(key)
    text_numbers = text_to_numbers(text, alph)

    rashifr_numbers = []
    for i in range(0, len(text_numbers), n):
        block = np.array(text_numbers[i:i + n]).reshape(n, 1)       #вектор
        rashifr_block = np.dot(key_obr, block) % len(alph)      #умножение на обр матрицу
        rashifr_numbers.extend(rashifr_block.flatten())
    return numbers_to_text(rashifr_numbers, alph)





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

    print(f"Введи {size}x{size} ключевую матрицу построчно через пробелы:")
    key = []
    for _ in range(size):
        row = list(map(int, input().split()))
        key.append(row)
    key = np.array(key)


    det = int(round(np.linalg.det(key)))        # проверка на НОД определителя и размера алфавита
    nod = math.gcd(det, len(alph))
    if nod != 1:
        print(f"Ошибка: НОД определителя матрицы ({det}) и размера алфавита ({len(alph)}) равен {nod}, а должен быть 1.")
        return



    if mode in ["шифрование", "шифр"]:
        result = hilla_shifr(text, key, alph)
        print("Зашифрованный текст:", result)
    elif mode in ["расшифрование", "расшифр"]:
        result = hilla_rashifr(text, key, alph)
        print("Расшифрованный текст:", result)
    else:
        print("Ошибка, неправильный режим.")







if __name__ == "__main__":
    main()
