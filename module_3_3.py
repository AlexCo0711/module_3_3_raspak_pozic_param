# Самостоятельная работа по уроку "Распаковка позиционных параметров".

# Task 1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(1, 'строка', True)
print_params()
print_params(9, 8, 7)
print_params(2, 6) # не указанный параметр (c) дополнился параметром по умолчанию
#print_params(3, 5, 7, 11) ошибка, аргументов больше чем параметров
print_params(b = 25) # не указанный параметр (a, c) дополнился параметром по умолчанию
print_params(c = [1,2,3]) # не указанный параметр (a, b) дополнился параметром по умолчанию

# Task 2
values_list = [False, 17, 'one'] # создан список
values_dict = {'a' : 'one', 'b' : 19, 'c' : True} # создан словарь
# def print_params2(a, b, c): # объявлена функция с параметрами
#    print(a, b, c)

print_params(*values_list) # передача в функцию распакованного списка
print_params(**values_dict) # передача в функцию распакованного словаря

# Task 3

def print_params3(*args): # объявлена функция с параметрами
    print(*args)

# исходные данные task 3
values_list_2 = [54.32, 'Строка' ]
print_params3(*values_list_2, 42)
