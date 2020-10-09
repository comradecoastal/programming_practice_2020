n = int(input())

synonyms = dict()

# заполняем словарь
for i in range(n):
    word1, word2 = input().split()
    synonyms[word1] = word2

word = input()

# проверяем словарь на сопадения
for word1, word2 in synonyms.items():
    if word1 == word:
        print(word2)
    if word2 == word:
        print(word1)