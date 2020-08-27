import re

word_regex = r"(\w+)(\W*)"

transliteration_map_capital = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'YO',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'Y',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TS',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ъ': '',
    'Ы': 'Y',
    'Ь': '',
    'Э': 'E',
    'Ю': 'YU',
    'Я': 'YA',
}

transliteration_map = {
    'А': 'A', 'а': 'a',
    'Б': 'B', 'б': 'b',
    'В': 'V', 'в': 'v',
    'Г': 'G', 'г': 'g',
    'д': 'd', 'Д': 'D',
    'Е': 'E', 'е': 'e',
    'Ё': 'Yo', 'ё': 'yo',
    'Ж': 'Zh', 'ж': 'zh',
    'З': 'Z', 'з': 'z',
    'И': 'I', 'и': 'i',
    'Й': 'Y', 'й': 'y',
    'К': 'K', 'к': 'k',
    'Л': 'L', 'л': 'l',
    'М': 'M', 'м': 'm',
    'Н': 'N', 'н': 'n',
    'О': 'O', 'о': 'o',
    'П': 'P', 'п': 'p',
    'Р': 'R', 'р': 'r',
    'С': 'S', 'с': 's',
    'Т': 'T', 'т': 't',
    'У': 'U', 'у': 'u',
    'Ф': 'F', 'ф': 'f',
    'Х': 'Kh', 'х': 'kh',
    'Ц': 'Ts', 'ц': 'ts',
    'Ч': 'Ch', 'ч': 'ch',
    'Ш': 'Sh', 'ш': 'sh',
    'Щ': 'Shch', 'щ': 'shch',
    'Ъ': '', 'ъ': '',
    'Ы': 'Y', 'ы': 'y',
    'ь': '', 'Ь': '',
    'Э': 'E', 'э': 'e',
    'Ю': 'Yu', 'ю': 'yu',
    'я': 'ya', 'Я': 'Ya',
}

endings_map = {
    "ый": "y",
    "Ый": "Y",
    "ыЙ": "Y",
    "ЫЙ": "Y",
    "кий": "ky",
    "Кий": "KY",
    "кИй": "KY",
    "киЙ": "KY",
    "КИй": "KY",
    "кИЙ": "KY",
    "КиЙ": "KY",
    "КИЙ": "KY",
    "": ""
}


def printf(str):
    print(str, end="")


def transpose(string):
    word_matches = re.finditer(word_regex, string, re.MULTILINE)
    for _, match in enumerate(word_matches):
        word = match.group(1)
        transpose_word(word)
        printf(match.group(2))
    print("")


def transpose_word(word):
    root = word
    ending = ""
    word_in_lower = word.lower()
    if word_in_lower.endswith("ый"):
        root = word[0:-2]
        ending = word[-2:]
    elif word_in_lower.endswith("кий"):
        root = word[0:-3]
        ending = word[-3:]

    for letter in root:
        if word.isupper():
            transpose_letter(transliteration_map_capital, letter)
        else:
            transpose_letter(transliteration_map, letter)

    printf(endings_map[ending])


def transpose_letter(dictionary, letter):
    printf(dictionary[letter])


if __name__ == '__main__':
    while True:
        text = input("Введите текст: ")
        transpose(text)