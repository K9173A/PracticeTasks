## Триггеры
В основном используются для внесения изменений в таблицы по определённому времени - на определённый момент времени
происходит действие, объединение определённых полей по определённым соотвествиям - БЭКАП.

```mysql
-- Создать триггер, который при добавлении нового сотрудника будет
-- выплачивать ему вступительный бонус, занося запись об этом в таблицу salary.
DELIMITER // 

DROP TRIGGER IF EXISTS bonus_adder_trg //

 CREATE TRIGGER bonus_adder_trg
AFTER INSERT ON employees
   FOR EACH ROW
          BEGIN
    INSERT INTO salaries (emp_no, salary, from_date, to_date)
         VALUES (NEW.emp_no, 10000, CURDATE(), CURDATE());
            END //
            
DELIMITER ;

-- Добавление записи
INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date)
     VALUES (2, '1988-08-08', 'John', 'Doe', 'M', CURDATE());

-- Проверка существования новых записей
-- SELECT * FROM employees WHERE emp_no = 2;
-- SELECT * FROM salaries WHERE emp_no = 2; 
```

* `DROP TRIGGER` - удаляет триггер с таким именем, если он существовал.
* `AFTER INSERT` - триггер будет срабатывать после вставки в таблицу `employees`.
* `FOR EACH ROW` - после данной строчки определеяется тело триггера.
* `NEW.emp_no` - новый сотрудник, который только-что был добавлен в БД.

