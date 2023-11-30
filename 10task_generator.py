# **Вычисление факториала числа.**
# Напишите функцию, которая вычисляет факториал числа n с использованием рекурсии.
# def factorial_of_number(value: int):
#   if value == 0:
#     return 1
#   result = factorial_of_number(value-1)
#   return result * value
#
# print(factorial_of_number(5))
 #________________________________________

# **Подсчет суммы элементов списка.**
# Напишите функцию, которая рекурсивно вычисляет сумму
# всех элементов списка целых чисел.

# numbers = [1, 2, 1, 5, 8, 3]
# def sum_elem(arg: list):
#   if len(arg) == 1:
#     return arg[0]
#
#   return sum_elem(arg[0: len(arg) - 1]) + int(arg[len(arg) - 1])
#
# print(sum_elem(numbers))

# **Вычисление чисел Фибоначчи.**
# Напишите функцию, которая рекурсивно вычисляет n-ное
# число в последовательности Фибоначчи.

# def fibonachi_fun(n):
#     if n == 1:
#         return 0
#     if n ==2:
#         return 1
#     return fibonachi_fun(n - 1) + fibonachi_fun(n - 2)
#
# print(fibonachi_fun(7))