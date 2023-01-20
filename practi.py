# 1

languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for language in languages:
    if language == 'Rust':
        print('This is language in list', language)
        break

# 2
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for language in languages:
    print(language)
    if language == "php":
        break

# 3
numb = 7 ** 5

for i in range(1, 6):
    print(7 ** i)

# 4
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
length = len(languages)
for i in range(length):
    print(i, languages[i])

# 5
for i in range(1, 10):
    print(i)

# 6
names:  = ('Максат', 'Лязат', 'Данияр', 'Айбек', 'Атай',
         'Салават', 'Адинай', 'Жоомарт', 'Алымбек',
         'Эрмек', 'Дастан', 'Бекмамат', 'Аслан')
count = len(names)
if names % 2 == 0:
    print(names)

# 7
names = ('Максат', 'Лязат', 'Данияр', 'Айбек', 'Атай',
         'Салават', 'Адинай', 'Жоомарт', 'Алымбек',
         'Эрмек', 'Дастан', 'Бекмамат', 'Аслан')
for i in range(1, 14, 2):
    print(i, names[i])

#
from random import randint, choice

symbols = "asdfghjkzxcvbnmqwertyuiol0123456789!@#$%^&*"

ent = int(input("enter length :"))

password_simbols = list()

for i in range(ent):
    random_char = symbols[randint(0, len(symbols) - 1)] # or random_char = choice(symbols)
    password_simbols.append(random_char)

print("".join(password_simbols))
