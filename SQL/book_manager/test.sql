alter table books modify book_id int;
alter table books auto_increment = 9;
alter table books modify book_id int auto_increment;
show table status like 'books'\G