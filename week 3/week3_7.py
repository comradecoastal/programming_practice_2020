rows = int(input())

words_counted = set([])

# для каждой строчки считываем список строк
for i in range(rows):
    words = [s for s in input().split()]

    for word in words:
        if word not in words_counted:  # если слово ранее не встречалось, то добавляем его в множество слов
            words_counted |= {word}

print(len(words_counted))
