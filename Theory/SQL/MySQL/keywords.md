## Частовстречаемые ключевые слова
### `DISTINCT`
Уникальное значение.
```mysql
SELECT DISTINCT title
           FROM regions;
```

### `WHERE`
Условие выбора.
```mysql
SELECT *
  FROM regions
 WHERE region_id = 10001;
```

### `IN`
Здесь мы берём все значения из таблицы `regions` по `regions_id`, но мы хотим выбрать только те, которые совпадают с
регионом России из таблицы `cities`, поэтому мы делаем выборку из таблицы `cities` в `regions_ru` и сравниваем с
выборкой по `region_id`.
```mysql
SELECT *
  FROM regions
 WHERE region_id 
    IN (
         SELECT region_ru
           FROM cities
       );  
```

### `BETWEEN`
Значение в определённом промежутке.
```mysql
 SELECT *
   FROM regions
  WHERE region_id
BETWEEN 10001 AND 10005;
```

### `NOT`
Отрицание.
```mysql
     SELECT *
       FROM regions
      WHERE region_id
NOT BETWEEN 10001 AND 10005;
```

### `LIKE`
Осуществляет поиск по строкам в примитивной форме.
```mysql
SELECT first_name
  FROM employees
 WHERE first_name
  LIKE '_____';
```
Нижнее подчёркивания определяют количество символов в строке.
`%` - плейсхолдер для любого количества символов.

### `REGEXP BINARY`
Поиск по регулярному выражению с учётом регистра (`BINARY`).
```mysql
       SELECT first_name
         FROM employees 
        WHERE first_name
REGEXP BINARY '^a';
```

### `GROUP BY`
Группировка по определённом столбцу.
```mysql
  SELECT max(salary)
       , concat(last_name, ', ', first_name) AS full_name
    FROM employees.employees
GROUP BY full_name;
```

### `HAVING`
Дополнительная выборка, полезна после `WHERE`.
```mysql
  SELECT max(salary)
       , concat(last_name, ', ', first_name) AS full_name
    FROM employees.employees
GROUP BY full_name
  HAVING emp_no
 BETWEEN 10001 AND 10005;
```

### `ORDER BY`
Сортировка по возрастанию или убыванию.
```mysql
  SELECT max(salary)
       , concat(last_name, ', ', first_name) AS full_name
    FROM employees.employees
GROUP BY full_name
  HAVING emp_no
 BETWEEN 10001 AND 10005
ORDER BY emp_no DESC;
```

### `LIMIT`
Ограничение количества результатов в выборке.
```mysql
  SELECT max(salary)
       , concat(last_name, ', ', first_name) AS full_name
    FROM employees.employees
GROUP BY full_name
  HAVING emp_no
 BETWEEN 10001 AND 10005
ORDER BY emp_no DESC
   LIMIT 4, 6;
```
Выдать с четвёртой строки 6 строк, то есть по 10-ю включительно.

### `LEFT JOIN`
* Выборка всех данных из первой таблицы (левой).
* Объединение с данными из второй таблицы (правой), которые совпадают с данными из первой таблицы.

### `RIGHT JOIN`
* Выборка всех данных из второй таблицы (правой).
* Объединение с данными из первой таблицы (левой), которые совпадают с данными из второй таблицы.

### `INNER JOIN`
Выборка совпадающих данных из обеих таблиц.
```mysql
-- Выбрать все города из Московской области.
	SELECT cities.title
      FROM cities
INNER JOIN regions
		ON cities.region_id = regions.id
	 WHERE regions.title = "Московская область";
```

### `FULL OUTER JOIN`
Выборка данных из обеих таблиц. Противоположность `INNER JOIN`.