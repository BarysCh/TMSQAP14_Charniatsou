alphabet_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
               'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_en_cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

alphabet_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
               'т', 'у', 'ф', 'х', 'ч', 'ш', 'щ', 'ъ', 'ю', 'я', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
               'т', 'у', 'ф', 'х', 'ч', 'ш', 'щ', 'ъ', 'ю', 'я']

alphabet_ru_cap = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С',
                   'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ь', 'Ю', 'Я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С',
                   'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ь', 'Ю', 'Я']


def encode(sentence, step):
    """encodes a sentence by shifting each word by a certain step"""
    new_sentence = ""
    new_letter = ""
    for letter in sentence:
        if letter in alphabet_en:
            position = alphabet_en.index(letter)
            new_letter = alphabet_en[position + step]
            new_sentence += new_letter
        elif letter in alphabet_en_cap:
            position = alphabet_en_cap.index(letter)
            new_letter = alphabet_en_cap[position + step]
            new_sentence += new_letter
        elif letter in alphabet_ru:
            position = alphabet_ru.index(letter)
            new_letter = alphabet_ru[position + step]
            new_sentence += new_letter
        elif letter in alphabet_ru_cap:
            position = alphabet_ru_cap.index(letter)
            new_letter = alphabet_ru_cap[position + step]
            new_sentence += new_letter
        else:
            new_sentence += letter

    return new_sentence


def decode(sentence, step):
    """decodes a sentence by shifting each word back by a certain step"""
    return encode(sentence, step * -1)


text = "Hello, my name is Boris"
encoded_message = encode(text, 1)

print(encoded_message)
print(decode(encoded_message, 1))







