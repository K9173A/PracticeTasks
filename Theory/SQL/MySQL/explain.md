### `EXPLAIN`
Инструкцию `EXPLAIN` удобно использовать, когда нужно увидеть "тонкие" места в таблице, где нужно что-то доработать,
изменить типы данных и т.п.

```mysql
USE employees;
EXPLAIN SELECT d.*
             , e.first_name
             , e.last_name
          FROM departments AS d
     LEFT JOIN dept_manager AS m 
            ON d.dept_no = m.dept_no
     LEFT JOIN employees AS e
            ON m.emp_no = e.emp_no;
```