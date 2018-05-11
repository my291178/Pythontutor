# Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

# Условие
# 1
# apple orange banana banana orange

# dictionary = {}
#
# q = int(input())
#
# for i in range(q):
#     words = input().split()
#
#     for i in words:
#         if i in dictionary:
#             dictionary[i] += 1
#         else:
#             dictionary[i] = 1
# # Подсчет и запись слов в словарь
# max_values = max(dictionary.values())
#
# # находим максимальное значение в лексикографическом порядке
# for key in sorted(dictionary.keys()):
#     # цикл по отсортированному по словам словарю
#     if dictionary[key] == max_values:
#         # если слово имеет максимальное значение
#         print(key)
#         break



PC = {'MAC': {'CPU': 2500, 'GPU': 1024, 'DDR3': 4000},
      'Intel': {'CPU': 1800, 'GPU': 512, 'DDR3': 3000},
      'AMD': {'CPU': 1500, 'GPU': 256, 'DDR3': 2000},
}
print(tuple(max(((itm[0], itm[1][key]) for itm in PC.items()), key=lambda t: t[1]) for key in set(sum((tuple(d.keys()) for d in PC.values()), ()))))