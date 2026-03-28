def vigenere_shifr(text, key, alph):
    shifr = ""
    key_len = len(key)      #длина ключа для повтора
    for i in range(len(text)):
        symbol = text[i]
        if symbol in alph:
            text_index = alph.index(symbol)
            key_index = alph.index(key[i % key_len])      #зацикливание ключа
            new_index = (text_index + key_index) % len(alph)    #шифрование
            shifr += alph[new_index]
        else:
            shifr += symbol
    return shifr














def vigenere_rashifr(text, key, alph):
    rashifr = ""
    key_len = len(key)
    for i in range(len(text)):
        symbol = text[i]
        if symbol in alph:
            text_index = alph.index(symbol)
            key_index = alph.index(key[i % key_len])    #расшифрование
            new_index = (text_index - key_index) % len(alph)
            rashifr += alph[new_index]
        else:
            rashifr += symbol
    return rashifr










def main():
    russian_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    english_alph = "abcdefghijklmnopqrstuvwxyz"

    language = input("Выбери язык (русский или английский): ").strip().lower()
    if language in ["русский", "рус"]:
        alph = russian_alph
    elif language in ["английский", "англ"]:
        alph = english_alph
    else:
        print("Неверный выбор языка.")
        return

    mode = input("Выбери режим (шифрование или расшифрование): ").strip().lower()

    if mode in ["шифрование", "шифр"]:
        key = input("Введи ключ-лозунг: ").strip().lower()
        if not all(char in alph for char in key):
            print("Ключ содержит недопустимые символы.")
            return

        text = input("Введи текст для шифрования: ").strip().lower().replace(" ", "")          #удаление пробелов из текста перед шифрованием
        result = vigenere_shifr(text, key, alph)
        print("Зашифрованный текст:", result)



    elif mode in ["расшифрование", "расшифр"]:
        key = input("Введи ключ-лозунг: ").strip().lower()
        if not all(char in alph for char in key):
            print("Ключ содержит недопустимые символы.")
            return

        text = input("Введи зашифрованный текст: ").strip().lower().replace(" ", "")          #удаление пробелов из зашифрованного текста
        result = vigenere_rashifr(text, key, alph)
        print("Расшифрованный текст:", result)

    else:
        print("Неподдерживаемый режим.")
















if __name__ == "__main__":
    main()