# Дан текст: в первой строке записано количество строк в тексте, а затем сами строки.
# Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте, а при одинаковой частоте появления — в лексикографическом порядке.
#
# Указание. После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова.
# Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов:
# частота встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')].
# Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу,
# а если они равны — то по второму. Это почти то, что требуется в задаче.

# Входные данные
# 9
# hi
# hi
# what is your name
# my name is bond
# james bond
# my name is damme
# van damme
# claude van damme
# jean claude van damme


n = int(input())

words = dict()
for i in range(n):
    for word in input().split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1


res = []

for key, value in words.items():
    # items позволяет взять из словаря массив из кортежей
    res.append( (value, key) )

# print(sorted(res))
nums = set(words.values())
# print(nums)

for num in sorted(nums, reverse=True):
    words_by_num = [i[1] for i in res if i[0] == num]
    for w in  sorted( words_by_num ):
        print(w)


