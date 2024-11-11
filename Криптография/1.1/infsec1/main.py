import string
import random
import math

# алфавит из букв русского и латинского алфавитов, цифр и спецсимволов
RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ENG = string.ascii_letters  # a-Z
ALPHABET = list(RU.lower() + RU + ENG + string.punctuation + string.digits + ' ')


# Функция генерации квадрата для шифрования
def generator(alphabet):
    random.shuffle(alphabet)
    return alphabet


# Функция для отображения квадратов
def show_square(square):
    for i in range(len(square)):
        if i % int(math.sqrt(len(square))) == 0:
            print()
        print(square[i], " ", end='')
    print("\n")


# Функция поиска позиции буквы
def get_letter_position(letter, square):
    position = square.index(letter)
    column, row = position % int(math.sqrt(len(square))), position // int(math.sqrt(len(square)))
    return column, row


# Функция шифрования/дешифрования биграммы
def crypto_bigramm(bigramma, first, second):
    try:
        # Позиции букв в квадратах
        first_letter_pos = get_letter_position(bigramma[0], first)
        second_letter_pos = get_letter_position(bigramma[1], second)
        # длина горизонтальной стороны
        side_length = int(math.sqrt(len(first)))
        _first = first_letter_pos[0] + second_letter_pos[1] * side_length
        _second = second_letter_pos[0] + first_letter_pos[1] * side_length
        if _first >= len(ALPHABET) or _second >= len(ALPHABET):
            return bigramma
        first_letter = first[_first]
        second_letter = second[_second]
        return first_letter + second_letter
    except IndexError:
        print(bigramma)
    return first_letter + second_letter


# Функция шифрования/дешифрования текста
def crypto(text, first, second):
    result = ""
    for i in range(0, len(text), 2):
        bigramma = ''.join(text[i:i + 2])
        result += crypto_bigramm(bigramma, first, second)
    return result


# Функция для чтения файла
def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


# Функция для записи в файл
def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)


def main():
    # текст, который необходимо зашифровать
    text_to_encrypt = read_file("text_to_encrypt.txt")
    if len(text_to_encrypt) % 2 != 0:
        text_to_encrypt += "КОНЕЦ"
    text_to_encrypt = list(text_to_encrypt)

    # создание квадратов
    first = generator(ALPHABET.copy())
    second = generator(ALPHABET.copy())
    # демонстрация сгенерированных квадратов
    print("Сгенерированные квадраты для шифрации:")
    print("Первый")
    show_square(first)
    print("Второй")
    show_square(second)

    # Шифрация текста
    encrypted_text = crypto(text_to_encrypt, first, second)
    # Сохранение зашифрованного текста
    write_file("encrypted_text.txt", encrypted_text)
    print(encrypted_text)

    # Получение текста, который необходимо дешифровать
    text_to_decrypt = read_file("encrypted_text.txt")
    # Дешифрация
    decrypted_text = crypto(text_to_decrypt, first, second)
    # Сохранение дешифрованного текста
    write_file("decrypted_text.txt", decrypted_text)
    print(decrypted_text)


if __name__ == '__main__':
    main()
