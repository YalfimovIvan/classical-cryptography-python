def vigenere_shifr_ciphertext_key(text, initial_key, alph):
    shifr = ""
    key_part = initial_key
    for i in range(len(text)):
        if i < len(key_part):           #создание ключа
            key_symb = key_part[i]
        else:
            key_symb = shifr[i - len(initial_key)]

        text_index = alph.index(text[i])
        key_index = alph.index(key_symb)
        new_index = (text_index + key_index) % len(alph)
        shifr += alph[new_index]
    return shifr












def vigenere_rashifr_ciphertext_key(shifrtext, initial_key, alph):
    rashifr = ""
    key_part = initial_key
    for i in range(len(shifrtext)):                    # Формирование самоключа
        if i < len(key_part):
            key_symb = key_part[i]
        else:
            key_symb = shifrtext[i - len(initial_key)]

        shifr_index = alph.index(shifrtext[i])
        key_index = alph.index(key_symb)
        new_index = (shifr_index - key_index) % len(alph)
        rashifr += alph[new_index]
    return rashifr











def main():
    russian_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    english_alph = "abcdefghijklmnopqrstuvwxyz"

    language = input("Выбери язык (русский или английский): ").strip().lower()
    alph = None
    if language in ["русский", "рус"]:
        alph = russian_alph
    elif language in ["английский", "англ"]:
        alph = english_alph
    else:
        print("Неверный выбор языка.")
        return




    mode = input("Выбери режим (шифрование или расшифрование): ").strip().lower()


    if mode in ["шифрование", "шифр"]:
        initial_key = input("Введите начальный ключ: ").strip().lower()
        if not initial_key:
            print("Ошибка: ключ не может быть пустым")
            return
        if not all(char in alph for char in initial_key):
            print("Ключ содержит недопустимые символы")
            return

        raw_text = input("Введите текст для шифрования: ").strip().lower()
        text = raw_text.replace(" ", "")
        if not text:
            print("Ошибка: текст не может быть пустым")
            return

        result = vigenere_shifr_ciphertext_key(text, initial_key, alph)
        print("Зашифрованный текст:", result)





    elif mode in ["расшифрование", "расшифр"]:
        initial_key = input("Введите начальный ключ: ").strip().lower()
        if not initial_key:
            print("Ошибка: ключ не может быть пустым")
            return
        if not all(char in alph for char in initial_key):
            print("Ключ содержит недопустимые символы")
            return

        raw_shifr = input("Введите зашифрованный текст: ").strip().lower()
        ciphertext = raw_shifr.replace(" ", "")
        if not ciphertext:
            print("Ошибка: шифртекст не может быть пустым")
            return

        result = vigenere_rashifr_ciphertext_key(ciphertext, initial_key, alph)
        print("Расшифрованный текст:", result)

    else:
        print("Неподдерживаемый режим")













if __name__ == "__main__":
    main()