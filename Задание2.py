# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.

# Входные данные
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye

dictionary = {}

q = int(input())
for i in range(q):
    key,value = input().split(" ")
    dictionary[key]=value

word = input()

for key,value in dictionary.items():
    if word == key:
        print (value)
        break
    if word == value:
        print (key)
        break