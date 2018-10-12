def is_end(arg):
    if arg == 'q':
        return(True)
    else:
        return(False)

print('''
# Пользователь вводит число,
# если оно четное - выбрасываем исключение ValueError,
# если оно меньше 0 - TypeError,
# если оно больше 10 - IndexError.
# Обрабатываем ошибку, говорим пользователю, в чем его ошибка
''')

def check_num(x):
    if x < 0:
        raise TypeError('Exception: Value < 0')
    elif x > 10:
        raise IndexError('Exception: Value > 10')
    elif x % 2 == 0:
        raise ValueError('Exception: Value % 2 = 0')

print('Enter \'q\' for break')
while True:
    try:
        inp_num = input('in: ')
        if is_end(inp_num):
            break
        check_num(float(inp_num))
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except IndexError as e:
        print(e)
print('-'*80)

print('''
# Создайте список произвольной длины.
# Пользователь должен ввести индекс объекта, который хочет посмотреть.
# Если все хорошо - пишите объект в консоль.
# Если нет - обработайте возмозможные ошибки и скажите ему, что не так
''')

def item_at(l, index):
    try:
        print(l[int(index)])
    except ValueError:
        print('Index = NaN')
    except IndexError:
        print('Wrong Index')

l = ['11', '22', '33', 44, 55, 66]
print('Enter \'q\' for break')
while True:
    inp = input('Index: ')
    if is_end(inp):
        break
    item_at(l,inp)
print('-'*80)

print('''
# Написать функцию, которая принимает на вход два аргумента.
# Если аргументы больше нуля, возвращаем их сумму.
# Если оба меньше - разность.
# Если знаки разные - возвращаем 0
''')

def sdz(a,b):
    if a > 0 and b > 0:
        return(a + b)
    elif a < 0 and b < 0:
        return(a - b)
    return(0)

print('Enter \'q\' for break')
while True:
    a = input('a: ')
    if is_end(a):
        break
    b = input('b: ')
    if is_end(b):
        break
    print('sdz = ', sdz(int(a), int(b)))
print('-'*80)

print('''
# Написать функцию, которая принимает 3 аргумента - числа,
# найти среди них два максимальных, вывести в консоль
''')

def max_func(a,b,c):
    l = [a,b,c]
    l.sort()
    print('answer is', l[2], 'and', l[1])

print('Enter \'q\' for break')
while True:
    a = input('a: ')
    if is_end(a):
        break
    b = input('b: ')
    if is_end(a):
        break
    c = input('c: ')
    if is_end(a):
        break
    max_func(a,b,c)
print('-'*80)

print('''
# Написать функцию, которая принимает два аргумента.
# Первый - список чисел, второй - булевый флаг.
# Если флаг действителен - возвращаем новый список с нечетными числами из входного списка,
# если флаг отрицателен - возвращаем новый список с четными числами из входного списка
''')

def func(nums,flag):
    odd = []
    even = []
    if int(flag):
        for num in nums:
            if num % 2 != 0:
                odd.append(num)
        return(odd)
    else:
        for num in nums:
            if num % 2 == 0:
                even.append(num)
        return(even)

while True:
    n = input('Enter \'q\' now for break or something else for continue: ')
    if is_end(n):
        break
    numbers =  map(int, input('Enter values separated by spaces: ').split(' '))
    f = input('Enter the flag: ')
    print(func(numbers, f))
print('-'*80)

print('''
# Написать функцию, которая принимает любое количество аргументов чисел.
# Среди них она находит максимальное и минимальное. И возвращает оба
''')

def min_max(*values):
    return(min(values),max(values))

print('min and max from min_max(4, 2, 5, -2, -2, 0, 6): ')
v = min_max(4, 2, 5, -2, -2, 0, 6)
print('min = {} and max = {}'.format(v[0],v[1]))
print('-'*80)

print('''
# Написать функцию, которая принимает два аргумента: строка и булевый флаг
#   case по-умолчанию равный True.
# Если флаг действителен: возвращаем новую строку, где каждый символ входной
#   строки приведен к верхнему регистру, иначе - к нижнему
''')

def case_func(s, case):
    if isinstance(s, str) and isinstance(case, bool):
        if case:
            return s.upper()
        else:
            return s.lower()

while True:
    n = input('Enter \'q\' now for break or something else for continue: ')
    if is_end(n):
        break
    text = input('Enter the string: ')
    f = input('Enter the case flag: ')
    print(case_func(str(text), bool(int(f))))
print('-'*80)

print('''
# Написать функцию, которая принимает любое количество позиционных аргументов -
#   строк и один парматер по-умолчанию glue, который равен ':'.
# Соединить все строки таким образом, чтобы в результат попали все строки,
#    длинее 3 символов.
# Для соединения между любых двух строк вставлять glue
''')

def func(*s, glue=':'):
    result = ''
    for word in s:
        if len(word) > 3:
            result += glue + word
    return str(result[1:])

print('args = \'Написать\',\'функцию\',\'которая\',\'все\',\'glue\'')
print('result = ', func('Написать','функцию','которая','все','glue'))
print('-'*80)
