Вход в БД:
```
psql -h localhost -U k9173a -d my_db;
```
Создание БД:
```postgresql
create database shop;
```
Проверка, что есть сейчас в БД:
```postgresql
\d
```
Создание таблицы:
```postgresql
create table customer(
    id serial primary key,
    name varchar(255),
    phone varchar(30),
    email varchar(255)
);
```
Будет создано две таблицы: `customer` и `customer_id_seq` (служебная таблица).
Можно посмотреть информацию по конкретной таблице:
```postgresql
\d customer
```
По аналогии создаём таблицу для продуктов:
```postgresql
create table product(
    id serial primary key,
    name varchar(255),
    description text,
    price integer
);
```
Можно проверить вторую таблицу, введя `\d product`. Создаём таблицу для фотографий продуктов:
```postgresql
create table product_photo(
    id serial primary key,
    url varchar(255),
    product_id integer references product(id)
);
```
Обратим внимание, что поле `product_id` является внешним ключом, который ссылается на поле `id` из таблицы `product`.
Создадим сущность корзины (заказа):
```postgresql
create table cart(
    customer_id integer references customer(id),
    id serial primary key
);
```
Создадим сущность товара в заказе, которая будет ассоциативной таблецй между `cart` и `product`:
```postgresql
create table cart_product(
    cart_id integer references cart(id),
    product_id integer references product(id)
);
```
Создадим какое-то количество клиентов:
```postgresql
insert into customer(name, phone, email) values ('Василий', '02', 'vac@gmail.com');
insert into customer(name, phone, email) values ('Петр', '03', 'vetr@gmail.com');
```
Выберем всех клиентов:
```postgresql
select * from customer;
```
Создадим два продукта:
```postgresql
insert into product (name, description, price) values ('iPhone', 'крутой телефон', 100000);
insert into product (name, description, price) values ('Apple watch', 'крутые часы', 50000);
```
Выберем все продукты:
```postgresql
select * from product;
```
Создадим фото продукта:
```postgresql
insert into product_photo (url, product_id) values ('iphone_photo', 1);
```
Выберем все фото:
```postgresql
select * from product_photo;
select url, product_id from product_photo;
```
Получим список из url и названием товаров. Здесь `pp` - это alias таблицы `product_photo`, а `p` - это alias таблицы
`product`.
```postgresql
   select pp.*
        , p.name
     from product_photo pp
left join product p on p.id=pp.product_id;
```
Таким образом мы соединини таблицы. Мы используем здесь `left join` - соответственно главной таблицей является левая
таблица (`product_photo`). И выборку из левой таблицы мы объединяем с данными из правой таблицы `product`.

Добавим фотографию на несуществующий продукт. Для этого нужно удалить FK
```postgresql
alter table product_photo drop constraint product_photo_product_id_fkey;
```
Теперь мы можем создать фотографию на несуществующий продукт (с индексом `100`):
```postgresql
insert into product_photo (url, product_id) values ('unknown_photo', 100)
```
Если сейчас повоторить запрос с `left join`, то в поле `name` будет `null`, так как продукт не существует.

Про join:
`inner join` - записи, присутствующие в обеих таблицах.
`left join` (`left outer join`) - записи, которые есть в левой таблице, и если из нет в правой таблице, то заполняются
`null`.
`right join` (`right outer join`) - это как `left join`, только наоборот. На практике используется крайне редко.

Если использовать `right join`, то основной таблицей будет правая, результат будет отзеркален.
```postgresql
    select pp.*
         , p.name
      from product_photo pp
right join product p on p.id=pp.product_id;
```
Но если использовать `inner join`, то будет выведена только одна запись, так как в расчёт берутся обе таблицы:
```postgresql
    select pp.*
         , p.name
      from product_photo pp
inner join product p on p.id=pp.product_id;
```
Удалим фото по `id`:
```postgresql
delete from product_photo where id=2;
```
Обновим фото:
```postgresql
update product_photo set url='iphone_image_2' where id=1;
```
Создадим заказ:
```postgresql
insert into cart (customer_id) values (1);
```
Добавление товара в корзину:
```postgresql
insert into cart_product (cart_id, product_id) values (1, 1), (1, 2);
```
У нас теперь два продукта в корзине:
```postgresql
select * from cart_product;
```
## Задачки
Имена клиентов с общей суммой их заказов.
```postgresql
   select c.name 
        , cart.id as cart_id
        , cp.product_id
        , p.price
     from customer c
left join cart on cart.customer_id=c.id
left join cart_product cp on cp.cart_id=cart.id
left join product p on p.id=cp.product_id;
```
Теперь нужно сгруппировать данные и просуммировать цены:
```postgresql
   select c.name 
        , sum(p.price)
     from customer c
left join cart on cart.customer_id=c.id
left join cart_product cp on cp.cart_id=cart.id
left join product p on p.id=cp.product_id
 group by c.name;
```
Если пользователь ничего не покупал, то у него будет `null`. Это не всегда удобно, поэтому в PostgreSQL есть функция
`coalesce()`, где вторым аргументом указывается значение, на которое нужно заменять, в нашем случае `0`:
```postgresql
   select c.name 
        , coalesce(sum(p.price), 0) as orders_sum
     from customer c
left join cart on cart.customer_id=c.id
left join cart_product cp on cp.cart_id=cart.id
left join product p on p.id=cp.product_id
 group by c.name;
```
Сортировка значений от самых больших заказов к самым маленьким:
```postgresql
   select c.name 
        , coalesce(sum(p.price), 0) as orders_sum
     from customer c
left join cart on cart.customer_id=c.id
left join cart_product cp on cp.cart_id=cart.id
left join product p on p.id=cp.product_id
 group by c.name
 order by orders_sum desc;
```
Фильтрация значений с помощью `having` - отличие его от `where` заключается в том, что он фильтрует группы. В `having`
всегда есть аггрегирующая функция. То есть делаем `where` - получаем строки. Делаем `group by` получаем группы, и если
нам эти сгруппированные значения нужно дополнительно отфильтровать, то применяем `having`:
```postgresql
   select c.name 
        , coalesce(sum(p.price), 0) as orders_sum
     from customer c
left join cart on cart.customer_id=c.id
left join cart_product cp on cp.cart_id=cart.id
left join product p on p.id=cp.product_id
 group by c.name
   having sum(p.price) > 0;
```
Иногда бывают проблемы с кодировками, поэтому сортировка может функционировать неправильно. В таком случае можно
использовать конструкцию: `~<~`. Если мы хотим выбрать только часть результатов, то используем `limit`:
```postgresql
   select *
     from customer
 order by name
    using ~<~
    limit 100;
```
Если нам нужна определённая запись или группа записей начиная с конкретного номера, то используем `offset`:
```postgresql
   select *
     from customer
 order by name
    using ~<~
    limit 1
   offset 1;
```