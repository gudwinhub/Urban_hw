import os
# print(os.getcwd())
# print(os.listdir())
#  Вариант работы с файлом, методы open-close
my_file = open('my_file.txt', 'w+', encoding='utf-8')
# опция w+  содержимое будет записано поверх существующего файла
# с опцией w файл создается только если не существовал до этого

my_file.write("""Пока свободою горим, 
Пока сердца для чести живы, 
Мой друг, отчизне посвятим
Души прекрасные порывы!""")
my_file.close()

my_file = open('my_file.txt', 'a+', encoding='utf-8')
my_file.write("""
\nТоварищ, верь: взойдет она,
Звезда пленительного счастья,
Россия вспрянет ото сна,
И на обломках самовластья
Напишут наши имена!""")
my_file.close()

# Вариант 2
# с использованием try/ finally - автоматическое закрытие при возникновении исключения

my_file = open('my_file.txt', 'a+', encoding='utf-8')
try:
    my_file.write('\nАС Пушкин')
finally:
    my_file.close()

# Вариант 3
#  с использованием инструкции with (автоматическое закрытие файла после выполнения действий)
# my_file = open('my_file.txt', 'a+')
with open('my_file.txt', 'a+', encoding = 'utf-8') as my_file:
    my_file.write('   1818 г')



my_file = open('my_file.txt', 'r', encoding='utf-8')
file_contents = my_file.read()
print(file_contents)

