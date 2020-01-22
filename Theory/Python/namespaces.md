Данный материал взят с ресурса:  https://devpractice.ru/closures-in-python/

## Области видимости
В Python выделяют четыре области видимости для переменных.

### Local
Эту область видимости имеют переменные, которые создаются и используются внутри функций.
```python
def add_two(a):
    x = 2
    return a + x

print(add_two(3)) # 5
print(x) # NameError: name 'x' is not defined
```
Внутри функции `add_two()` используется переменная `x`, доступ к которой снаружи невозможен. Эта переменная находится в
стеке функции и удаляется каждый раз, когда завершается `add_two()`.

### Enclosing
Внутри одной функции могут быть вложены другие функции и локальные переменны. Локальные переменные функции для её
вложенной функции находятся в enclosing области видимости.
```python
def add_two(a):
    x = 2
    def add_some():
        print(f'x = {x}')
        return a + x
    return add_some()

print(add_two(5))
# x = 2
# 7
```

### Global
Переменные данной области видимости - это глобальные переменные уровня модуля (модуль - это файл с расширением `.py`).
```python
x = 4

def fun():
    print(x + 3)

fun() # 7
```
В преведённом выше примере переменная x является глобальной. Доступ к ней можно получить из любой функции данного
модуля. А из другого модуля нельзя, так как для них она не будет являться глобальной.

### Built-in
Уровень Python интерпретатора. Туда входят функции `open()` и `len()`, исключения. Эти сущности доступны в любом модуле
Python и не требуют предварительного импорта. Built-in - это максимально широкая область видимости.

