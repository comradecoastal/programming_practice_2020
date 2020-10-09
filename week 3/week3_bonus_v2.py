import string

words_counts = dict()

# открываем файл с текстом
input_file = open('input_text.txt', 'r')
output_file = open('output_text.txt', 'w')

# считываем текст
read_data = input_file.read()

# удалём все небуквенные элементы из строки
for char in string.punctuation + string.digits:
    read_data = read_data.replace(char, ' ')

# делаем все буквы строчными
read_data = read_data.lower()

# подсчёт слов в тексте
for word in read_data.split():
    if word in words_counts:
        words_counts[word] += 1
    else:
        words_counts[word] = 1

# выод слов в алфавитном порядке
for word in sorted(list(words_counts.keys())):
    output = word + ' : ' + str(words_counts[word]) + '\n'
    output_file.write(output)
