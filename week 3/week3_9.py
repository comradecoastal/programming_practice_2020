words_counts = dict()
max_words = []
max_value = 0

n = int(input())

# для всех слов во всех строках считаем их количество и добавляем их в словарь
for i in range(n):
    for word in input().split():
        if word in words_counts:
            words_counts[word] += 1
        else:
            words_counts[word] = 1
        if words_counts[word] > max_value:
            max_value = words_counts[word]

# ищем слова, количество которых равно максимальному
for word, count in words_counts.items():
    if count == max_value:
        max_words.append(word)

# сортируем слова в лексикографическом порядке
max_words.sort()

# выводим первое слово в списке
print(max_words[0])
