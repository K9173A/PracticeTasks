## Типы данных

### `int`
#### Название
Целые числа.
#### Пример 
```python
my_var_1 = 2
my_var_2 = -5
my_var_3 = 0
```

### `float`
#### Название
Числа с плавающей точкой.
#### Пример
```python
my_var_1 = 2.6
my_var_2 = -5.2
```

### `complex`
#### Название
Комплексные числа.
#### Пример
```python
my_complex_number = complex(1, 2)
```

### `str`
#### Название
Строки.
#### Виды строк
Есть как обычные строки, так и строки, которые можно расположить на нескольких строчках.
Можно использовать как одинарные кавычки, так и двойные - это не влиет на функционал.
```python
str_one = 'Hello'
str_two = "Two"
str_three = '''
    Multiline string 1
'''
str_four = """
    Multiline string 2
"""
```
#### Методы строк
Перевести строку в верхний регистр:
```python3
'hello world'.upper() # HELLO WORLD
```
Перевести строку в нижний регистр:
```python3
'HELLO WORLD'.title() # hello world
```
Найти подстроку в строке:
```python3
'строка'.find('подстрока')
'строка'.rfind('подстрока')
'строка'.find('подстрока', 'индекс')
```
#### Форматирование строк
Использование сложения, можно суммировать с переменными, если они являются `str`:
```python
my_var = 'my dear'
print('Hello ' + my_var + ' World') # "Hello my dear World"
```
Вставка с помощью символа `%`, в скобках перечисляются данные для вставки, а в строке
указываются `%s` (строки) и `%d` (числа), на их место будет вставлены данные:
```python
my_var_1 = 1
my_var_2 = 'Hello World'
my_var_3 = False
print('%s %s %s' % (my_var_1, my_var_2, my_var_3)) # "1 Hello World False"
print('%d %d' % (my_var_1, my_var_3)) # "1 0" <- False = 0
```
Новый формат вставки. Используется метод `.format()`, в котором перечисляются данные для вставки.
В самой строке указываются скобки, на их место будет вставлены данные:
```python
print('{} {}'.format(1, 42)) # "1 42"
```
Можно менять последовательность аргументов `.format()` при вставке. Порядок указывается в скобках:
```python
print('{1} {0}'.format(1, 42)) # "42 1"
```
Можно указывать именованные аргументы:
```python
print('{my_named_var}'.format(my_named_var=42)) # "42"
```
Можно указать количество знаков после запятой у `float`:
```python
number = 23.8589578
print('{:.2f}'.format(number)) # 23.86 
```
Выравнивание в строке:
```python
print('{:>9}'.format('Foo')) # "      Foo"
print('{:9}'.format('Foo')) # "Foo      "
print('{:^9}'.format('Foo')) # "   Foo   "
```
Можно выбирать символ для отступа:
```python
print('{:_^9}'.format('Foo')) # "___Foo___"
```
Обрезка строк:
```python
print('{:.4}'.format('Hello')) # "Hell"
```
Обрезка и выравнивание:
```python
print('{:10.4}'.format('Hello')) # "Hell      "
```
Передача чисел и их выравнивание:
```python
print('{:d}'.format(42)) # "42"
print('{:f}'.format(42.22222222)) # "42.222222"
print('{:4d}'.format(42)) # "  42"
print('{:07.3f}'.format(42.22222222)) # "0042.22"
```
Знаки чисел и их выравнивание:
```python
print('{:+d}'.format(42)) # "+42"
print('{: d}'.format(-42)) # "-42"
print('{:=+3d}'.format(42)) # "+  42"
print('{:=3d}'.format(-42)) # "-  42"
```
Доступ к содержимому коллекций:
```python
person = {
    'first_name': 'John',
    'last_name': 'Doe',
}
print('p[first_name]} {p[last_name]}'.format(p=person))
numbers = [1, 2, 42]
print('{n[0]} {n[2]}'.format(n=numbers)) # "1 42"
```
Доступ к атрибутам:
```python
class Foo:
    my_attr = {'bar': 'Hello World', 'baz': 42}

print('{foo.my_attr[bar]}'.format(foo=Foo()))
```
Дата и время:
```python
from datetime import datetime
print('{:%Y-%m-%d %H:%M}'.format(datetime(2019, 7, 7, 7, 7))) # 2019-07-07 07:07
```
Параметризация:
```python
print('{:{align}{width}}'.format('foo', align='^', width='9')) # "   foo   "
print('{:.{prec}} {:.{prec}f}'.format('Foo', 2.22222, prec=2)) # "Fo 2.22"
print('{:{width}.{prec}f}'.format(2.7182, width=5, prec=2)) # " 2.72"
print('{:{}{}{}.{}}'.format(2.71, '>', '+', 10, 3)) # "     +2.72"
```
В свежих версиях Python появились f-строки:
```python
my_var = 5
print(f'{my_var}th') # "5th"
```

### `bool`
#### Название
Логический тип.
#### Пример
```python
this_is_true = True
this_is_false = False
```

### `None`
#### Название
Неопределённый тип данных.
#### Пример
```python
my_var = None
```
Если у функции нет `return None`, то он в любом случае будет возвращён.
```python
def foo():
    pass

print(foo()) # None
```
