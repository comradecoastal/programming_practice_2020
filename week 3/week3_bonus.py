import string

words_counts = dict()

while True:
    # пытаемся считать строку, если это не получается разрываем цикл
    try:
        line = input()
    except EOFError:
        break

    if 'END_OF_INPUT' in line:  # маркер конца ввода
        break

    # удалём все небуквенные элементы из строки
    if not line.isalpha():
        for char in string.punctuation + string.digits:
            line = line.replace(char, ' ')

    # делаем все буквы строчными
    line = line.lower()

    # подсчёт слов в строке
    for word in line.split():
        if word in words_counts:
            words_counts[word] += 1
        else:
            words_counts[word] = 1

# выод слов в алфавитном порядке
for word in sorted(list(words_counts.keys())):
    print(word, ':', words_counts[word])
