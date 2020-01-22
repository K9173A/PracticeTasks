## Функции
Функция что-то возвращает.
```mysql
-- Создать функцию, которая найдет менеджера по имени и фамилии.
DELIMITER // 

DROP FUNCTION IF EXISTS find_manager //

CREATE FUNCTION find_manager(
    manager_first_name VARCHAR(14),
    manager_last_name VARCHAR(16)
)
RETURNS INT(11) 
READS SQL DATA 
BEGIN
RETURN (	
         SELECT emp_no
           FROM dept_manager
          WHERE emp_no
             IN (
                  SELECT emp_no 
                    FROM employees
                   WHERE first_name = manager_first_name
                     AND last_name = manager_last_name
                )
       );
END //

DELIMITER ;

-- Сотрудник, но не менежер (пустой результат)
SELECT find_manager('Parto', 'Bamford');
-- Сотрудник, который является менеджером
SELECT find_manager('Margareta', 'Markovitch'); 
```

* `DELIMITER //` - ограничитель начала и конца функции.
* `RETURNS INT(11)` - возвращаемое из функции значение.
* `READS SQL DATA ` - инструкция, которая говорит MySQL, что функция будет лишь читать даные, но не модифицировать.
    * `MODIFIES SQL DATA` - аналогично, только для записи, удаления или изменения данных.
    * `NO SQL` - полное отсутствие каких-либо SQL выражений.
    * `CONTAINS SQL` - имеются SQL инструкции, но не содержатся выражения, которые бы читали или изменяли данные.
* `DELIMITER ;` - заменяем ограничитель на стандартный, чтобы последующие вызовы были отделены `;`.
* `BEGIN` и `END` - начало и конец функции.

## Процедуры
Процедура ничего не возвращает. Существует 4 типа процедур:

* Процедура без параметров.
* Процедура с параметром `IN` (input).
* Процедура с параметром `OUT` (output).
* Процедура с параметром `IN-OUT` (input/output).

```mysql
DELIMITER //
CREATE PROCEDURE display_book()
BEGIN
SELECT * FROM book;
END //

DELIMITER ;

CALL display_book();
```