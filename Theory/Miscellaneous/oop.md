Материал взят с ресурса: https://ru.wikipedia.org/wiki/Объектно-ориентированное_программирование

## ООП
ООП - это набор парадигм и идей.

### Абстракция
Выделение значимой информации и исключение из рассмотрения незначимой. В ООП рассматривают лишь абстракцию данных
(нередко называя её просто «абстракцией»), подразумевая набор наиболее значимых характеристик объекта, доступных
остальной программе.

### Полиморфизм
Свойство системы, позволяющее использовать объекты с одинаковым интерфейсом без информации о типе и внутренней структуре
объекта. Другой вид полиморфизма — параметрический — в ООП называют обобщённым программированием.

* При статической типизации сложнее допустить ошибку. Она безопаснее и в некоторых ситуациях быстрее.
* Динамическая типизация даёт больше возможностей прострелить себе колено.
* Перегрузки функций - ad hoc полиморфизм.

Полиморфизм нужен в ситуации, как в следующей:
```c++
// Классы героев
class FirstHero {}
class SecondHero {}
class ThirdHero {}

// Класс команды - подборка героев может быть разная
// Предётся перегружать конструктор - все возможные сочетания героев! Убийство!
class Team {
	Team(FirstHero h1, SecondHero h2, ThirdHero h3) { /* Code */ }
	Team(FirstHero h1, FirstHero h2, ThirdHero h3) { /* Code */ }
	// ...
	Team(ThirdHero h1, ThirdHero h2, ThirdHero h3) { /* Code */ }
}
```
С полиморфизмом:
```
class Hero

class FirstHero : public Hero {}
class SecondHero : public Hero  {}
class ThirdHero : public Hero {}

class Team {
	Team(Hero h1, Hero h2, Hero h3) { /* Code */ }
}
```

### Наследование
Свойство системы, позволяющее описать новый класс на основе уже существующего с частично или полностью заимствующейся
функциональностью. Класс, от которого производится наследование, называется базовым, родительским или суперклассом.
Новый класс — потомком, наследником, дочерним или производным классом.

### Инкапсуляция
Свойство системы, позволяющее объединить данные и методы, работающие с ними, в классе.