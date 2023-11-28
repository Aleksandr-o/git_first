# Написать ф-цию, которая возвращает замыкание для вычесления факториала.
# def factoreal(val):
#     def inner_calculator():
#         res = 1
#         for i in range(2, val+1):
#             res *=i
#         return res
#     return inner_calculator
#
# get_result = factoreal(5)
# print(get_result())
#####################################################################
# #2) Создать функцию для генерации случайных паролей с заданной длиной, используя замыкания.
# import random
#
# chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# def generator_random_keys(length):
#     password =''
#     def work_generator():
#         nonlocal password
#         for i in range(length):
#           password += random.choice(chars)
#
#         return password
#     return work_generator
# get_random_key = generator_random_keys(15)
# print(get_random_key())
###############################################################################
# 3) Написать декоратор на валидацию пароля. Этот декоратор должен
# применяться к функции, которая пароль запрашивает.
# Если всё хорошо - выводить сообщение о том, что пароль валиден,
# в противном случае вывести, что что-то не так. (или кто захочет -
# вывести конкретное сообщение, что в пароле не так.)
# _^s@#$1kL10

# import re
# def my_decorator(func):
#   def wrapper(*args):
#       if len(*args) < 8:
#           print("пароль не соответствует по длине")
#       else:
#           if not re.search(r'[A-Z]', *args):
#               print("пароль не содержит заглавную букву")
#           else:
#               if not re.search(r'[a-z]', *args):
#                   print("пароль не содержит строчную букву")
#               else:
#                   if not re.search(r'[0-9]', *args):
#                       print("пароль не содержит цифру.")
#                   else:
#                       if not re.search(r'[\-!@#$%^&*?_|<>{}]', *args):
#                           print("пароль не содержит символ.")
#
#       return func(*args)
#   return wrapper
# @ my_decorator
# def password_validator(password):
#   if len(password) > 8:
#     if re.search(r'[A-Z]', password):
#       if re.search(r'[a-z]',password):
#         if re.search(r'[0-9]', password):
#           if re.search(r'[\-!@#$%^&*?_|<>{}]', password):
#             print("пароль валиден")
#
# password_validator(input("Введите ваш паролЪ: "))


# import re
# def password(data):
#     return not (len(data) < 8 or
#             data.isdigit() or
#             data.isalpha() or
#             data.islower() or
#             data.isupper() or not
#             re.search(r'[\-!@#$%^&*?_|<>{}]', data))
#
# result = password('123Pass_Word!')
# print(result)
#
#

########################################################################
# 4) Когда-то давно была задача на расчёт индекса массы-тела.
# Перепишите эту задачу с использованием замыканий.

# def BMI_calculate(weight, height):
#     weight = weight
#     height = height
#     def inner_calculate():
#         BMI = weight / (height ** 2)
#         if 18.5 < BMI < 25:
#             print(f"Норма {BMI:.0f}")
#         elif 16 < BMI < 18.5:
#             print(f"Недостаточный вес {BMI=:.0f}")
#         elif 25 < BMI < 30:
#             print(f"Избыточный вес {BMI=:.0f}")
#         elif 30 < BMI < 35:
#             print(f"Ожирение {BMI:.0f}")
#         else:
#             print("Введите реальные данные")
#
#     return inner_calculate
#
# result = BMI_calculate(float(input("Вес (кг): ")), float(input("Рост (м): ")))
# result()
#
# # 4) """11**Калькулятор BMI (Индекс массы тела):**
# # Запросите у пользователя его вес (кг) и рост (м).
# # Рассчитайте его BMI по формуле BMI = вес / (рост^2) и выведите сообщение,
# # указывающее на его состояние: "Недостаточный вес", "Норма", "Избыточный вес", "Ожирение"."""try:
#     weight = float(input("Вес (кг): "))
#     height= float(input("Рост (м): "))
#     BMI = weight / (height ** 2)
#     if 18.5<BMI<25:
#         print(f"Норма {BMI:.0f}")
#     elif 16<BMI<18.5:
#         print(f"Недостаточный вес {BMI=:.0f}")
#     elif 25<BMI<30:
#         print(f"Избыточный вес {BMI=:.0f}")
#     elif 30<BMI<35:
#         print(f"Ожирение {BMI:.0f}")
#     else:
#         print("Введите реальные данные")
#
# except (ValueError, ZeroDivisionError):
#     print("Попытка деления числа на ноль или некорректный ввод")
##############################################################################
# 5) Напишите декоратор, который будет применяться к функции,
# выводить информацию типа: какая функция была вызвана, какие
# у неё были параметры, сколько раз она была вызвана.


#############################################################################
# 6) Напишите декоратор, который замеряет время выполнения вашей
# функции. Если время выполнения в пределах двух секунд - выводите
# что всё хорошо. В противном случае сообщение о том, что функция
# (её имя) работает слишком медленно, её необходимо оптимизировать.
#
# from datetime import datetime
#
# def measure_decor(func):
#     def wrapper(*args):
#         time_start = datetime.now()
#         print(f"Старт выполнения функции {time_start}")
#         func(*args)
#         time_stop = datetime.now()
#         print(f"Конец выполнения функции {time_stop}")
#         time_delta = time_stop - time_start
#         print(type(time_delta))
#         sec = time_delta.seconds
#         print(sec)
#         if sec > 2:
#           print(f"функция {func} работает слишком медленно, её необходимо оптимизировать.")
#         else:
#           print("Все хорошо")
#         return time_delta
#     return wrapper
#
# @measure_decor
# def my_fuction1(value1):
#     res = [elem *357 if elem%2==0 else elem *1.5 for elem in range(1, value1)]
#     return res
#
# @measure_decor
# def my_function2(step):
#     for item in range(1, step):
#         result_list1 = []
#         result_list2 = []
#         if item % 5 ==0:
#             result_list1.append(item)
#         else:
#             result_list2.append(item**870)
#     return result_list1, result_list2
#
# my_fuction1(110000000)
# my_fuction1(10000000)


