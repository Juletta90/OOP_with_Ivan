# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/





# days = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')  # кортеж
# steps = [1500, 3445, 13222, 10000, 12555, 1300, 6000]  # список
#
# result = []



# Как сравнить ВСЕ элементы друг с другом? Например, есть два списка.
#
# lst_1 = [2,4,8,16,12]
# lst_2 = [4,6,12,1,8]
# Создаем пустой список. Создаем цикл для первого списка. Добавляем условие: если i есть во втором списке то добавляем его в третий список.
#
# lst_3 = []
#
# for i in lst_1:
#     if i in lst_2:
#         lst_3.append(i)
# print(lst_3)
# Результат: [4,12,8]


#_______________________________________________
# Вычислите и напечатайте количество одинаковых элементов в коллекциях num_string_1 и num_string_2.

num_string_1 = '100 13 2 143 12 3 55 4 64 18 56'
num_string_2 = '234 2 56 432 3 100 12 99 43 18 31 64'

str_to_set_1 = num_string_1.split()
str_to_set_2 = num_string_2.split()

num_string_3 = set(str_to_set_1) & set(str_to_set_2)
print(len(num_string_3))

print()
print()
#______________________________________________

# Антон получил в ответ от сервера перечень ID клиентов в виде строки,
# где ID  разделены пробелами. Его задача — удалить дубликаты и отсортировать список ID по возрастанию.
# Напишите программу, которая поможет Антону формировать такие списки.
# Если в списке будет найден дублирующийся ID — программа должна вывести
# в терминал сообщение «Найден дубликат ID <значение_id>».

id_string = '32 48 2 6 14 58 2 88 9 14 123 48 3 17 42 42 7'
empty_set = set()
num_set = set()  # множество для числовых значений
split_string = id_string.split()  # преобразование строки в список
#print(split_string)


for num in split_string:
    if num in empty_set:
        print(f'Найден дубликат ID {num}')
    else:
        empty_set.add(num)
        num_set.add(int(num))   # преобразование строк в числа

num_set_sorted = sorted(num_set)
print(num_set_sorted)

#_________________________________________________

# Функция-упаковщик zip() принимает в качестве аргументов итерируемые объекты,
# а возвращает объект типа zip — это коллекция кортежей.
# Каждый из кортежей содержит элементы исходных коллекций с одинаковыми индексами.

# Однако обращаться к элементам zip-объекта можно точно так же, как и к элементам любой другой последовательности.
# Объекты типа zip — итерируемые.

# Переберите в цикле элементы объекта movies_info и напечатайте их.

movie_ratings = [4.7, 5.0, 4.3, 4.0]
movies = ['Матрица', 'Хакеры', 'Трон', 'Кибер']

movies_info = zip(movies, movie_ratings)

for films in movies_info:
    print(films)

#_______________________________________________


movies = {
    'Матрица': {'rating': '4.7', 'review': 'Фильм крут'},
    'Хакеры':  {'rating': '4.5', 'review': 'Смотреть можно'},
    'Трон':  {'rating': '3.8', 'review': 'Смотреть можно'},
    'Кибер':  {'rating': '2.5', 'review': 'Так себе киношечка'},
    'Пятая власть':  {'rating': '4.1', 'review': 'Смотреть можно'},
}

hackers = movies['Хакеры']

print(hackers['rating'], hackers['review'])


print()
#_______________________________________________


# Онлайн-кинотеатр присылает Антону перечень фильмов, рекомендованных к просмотру.
# Помогите Антону выбрать фильмы с высоким рейтингом и добавить в избранное.

# Если рекомендованный фильм имеет рейтинг ниже 4.0 — удалите его из словаря recommended_movies.

# При этом программа должна вывести сообщение
# Фильм "<название_фильма>" не интересен: "<отзыв_о_фильме>". Фильм удалён из рекомендаций.

# Все фильмы с рейтингом выше 4.0 программа должна добавить в словарь
# с избранными фильмами favorite_movies и вывести сообщение

# У фильма "<название_фильма>" хороший отзыв: "<отзыв_о_фильме>". Фильм добавлен в избранное.
# Напечатайте получившуюся коллекцию избранных фильмов.

favorite_movies = {}

recommended_movies = {
    'Хенкок': {'rating': 4.5, 'review': 'Смотреть можно'},
    'Матрица': {'rating': 4.7, 'review': 'Фильм крут'},
    'Кибер': {'rating': 2.5, 'review': 'Так себе киношечка'},
    'Трон': {'rating': 3.8, 'review': 'Так себе киношечка'},
    'Мстители': {'rating': 4.7, 'review': 'Фильм крут'},
    'Хакеры':  {'rating': 4.5, 'review': 'Смотреть можно'}
}

# место для вашего кода
for movie, rating in recommended_movies.items():
    if rating < str(4):
        print(f'Фильм {movie} не интересен: {review}. Фильм удалён из рекомендаций. ')
    rating_review = recommended_movies.get(movie)   # Вывод в терминал: {'rating': 4.5, 'review': 'Смотреть можно'}
    #print(rating_review)


    for name, review in rating_review.items():
        print(f'Фильм {movie} не интересен: {review}')





print(favorite_movies)