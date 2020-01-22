## Генераторы
Что это такое:

* Итераторы являются синтаксическим сахаром в некоторых языках.
* Итератор также является паттерном проектирования, описанным в списке "Банды четырёх".
* Данная практика используется повсеместно в разных языках программирования, поэтому знать её полезно.
* Итераторы являются одним из примеров интерфейса.

Примеры использования:

* Генерация случайных чисел.
* Итерация через матрицы или таблицы данных.

### Что является итератором в Python?
Итератор - это объект, у которого определены следующие методы:

#### `__iter__()`
* Это метод, который возвращает итерируемый объект, то есть объект, для которого определён метод `__next__()`.
* Работает по принципу замыкания функции.

#### `__next__()`
* В данном методе нужно отразить логику вытаскивания следующего элемента.
* Когда программист пишет логику, ему потребуется создать счётчик, чтобы запоминать состояние итерируемого объекта. В
этом и вся магия "запоминания". Стоит отметить, что `yield` здесь использовать не нужно!
* В старых версиях Python в конце нужно было писать `raise StopIteration`, теперь этого делать не нужно!

### Варианты реализации
Могут быть два варианта реализации:

#### Вариант 1
В следующем случае возвращается ссылка на сам класс. Этим мы говорим, что мы в данном классе реализовали метод
`__next__()` и можно итерацию совершать через сам класс.
```python
class Colors:
	def __init__(self, colors):
		self.colors = colors
		self.i = 0

	def __iter__(self):
		return self

	def __next__(self):
		self.i += 1
		if self.i == len(self.colors):
			self.i = 0
		return self.colors[self.i]
```

#### Вариант 2
В следующем случае вызывается метод `iter()` у внутреннего контейнера. Этим мы говорим, что хотим использовать
возможность итерироваться только лишь по внутреннему контейнеру, но не по классу. Класс здесь выступает лишь в качестве
фасада.
```python
class Colors:
	def __init__(self, colors):
		self.colors = colors # Это list()

	def __iter__(self):
		return iter(colors)
```

### Аналогичные строки
Вызовы следующих методов является равносильным, но стоит использовать вариант 1.

| Вариант 1 | Вариант 2 |
|:--:|:--:|
| `iter(collection)` | `collection.__iter__()` |
| `next(collection_iterator)` | `collection_iterator.__next__()` |

### Примеры использования
#### Использование в цикле fot-in
Такие объекты, как списки, словари, строки умеют возвращать свои итераторы, поэтому по ним можно итерироваться. Когда мы
используем конструкцию for-in, справа от in стоит итерируемый объект - в неявной форме вызывается метод `iter()`:
```python
colors = ['red', 'yellow', 'green']
for color in colors:
	print(color)
```
Из-за этого следующая строка будет эквивалентной:
```python
colors = ['red', 'yellow', 'green']
for color in iter(colors):
	print(color)
```

#### Итерация с помощью `next()`
```python
my_list = [1, 4, 6, 10]
my_list_iter = iter(my_list)
print(next(my_list_iter)) # 1
print(next(my_list_iter)) # 4
# ...
print(next(my_list_iter)) # StopIteration
```
Цикл останавливается, когда итератор выкидывает исключение `StopIteration`.

### `itertools`
Библиотека `itertools` - содержит различные функции для работы с итерируемыми объектами.

#### `chain()`
Позволяет объединить два итератора в один. Итерация происходит вначале по первой коллекции, а потом по второй.
```python
l1 = iter([1, 2, 3])
l2 = iter([4, 5])
for elem in itertools.chain(l1, l2):
	print(elem)
```

#### `cycle()`
Позволяет бесконечно выполнять заданную последовательность.
```python
colors = ['r', 'g', 'b']
for color in itertools.cycle(colors):
	print(color) # r g b r g b r g b ...
```

#### `count()`
Выдаёт числа начиная с указанного и до бесконечности.
```python
itertools.count(2)
```

### Примеры
Генератор случайных чисел:
```python
import random

class RandNumbers:
    num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        if self.num > 100:
            raise StoppIteration
        return random.randint(-10, 10)
```