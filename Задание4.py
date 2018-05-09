# Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

# Условие
# 1
# apple orange banana banana orange

dictionary = {}

q = int(input())

for i in range(q):
    words = input().split()

    for i in words:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
# Подсчет слов в словаре

max_values = max(dictionary.values())
# находим максимальное значение

for key in sorted(dictionary.keys()):
    # цикл по отсортированному по словам словарю
    if dictionary[key] == max_values:
        # если слово имеет максимальное значение
        print(key)
        break
