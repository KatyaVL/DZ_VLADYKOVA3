#2.Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения,город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.


def personal_data(*, name, lastname, year_of_birth, city, email, phone):
    return print(f"Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth} Город проживания: {city} Email: {email} Телефон: {phone}")


personal_data(name=input('Имя: '),lastname=input('Фамилия: '), year_of_birth=input('Год Рождения: '),
    city=input('Город проживания: '),email=input('email: '),phone=input('phone: '),)