create table if not exists books (
    book_id int primary key auto_increment,
    book_name nvarchar(40) not null,
    author nvarchar(40),
    price int,
    status tinyint not null
);

create table if not exists users (
    user_id int primary key auto_increment,
    user_name varchar(40) not null,
    password varchar(30) not null,
    birthday date
);

create table if not exists l_r_log (
    record_id int primary key auto_increment,
    user_id int not null,
    book_id int not null,
    l_r tinyint not null,
    date date default (curdate())
);

create table if not exists lend_status (
    record_id int primary key auto_increment,
    user_id int not null,
    book_id int not null,
    date date not null default (curdate())
);

create table if not exists status_explain (
    status tinyint,
    status_name varchar(20)
);

create table if not exists l_r_explain (
    l_r tinyint,
    l_r_name varchar(20)
);