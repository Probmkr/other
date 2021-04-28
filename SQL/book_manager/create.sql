create table if not exists books (
    book_id int primary key auto_increment,
    book_name nvarchar(40) not null,
    author nvarchar(40),
    price int,
    status tinyint not null default (1)
);

create table if not exists users (
    user_id int primary key auto_increment,
    user_name varchar(40) not null,
    password varchar(30) not null,
    birthday date
);

create table if not exists b_r_log (
    record_id int primary key auto_increment,
    user_id int not null,
    book_id int not null,
    b_r tinyint not null,
    date date default (curdate()),
    foreign key book_id_fk (book_id) references books (book_id),
    foreign key user_id_fk (user_id) references users (user_id)
);

create table if not exists borrow_status (
    record_id int primary key auto_increment,
    user_id int not null,
    book_id int not null,
    date date not null default (curdate()),
    foreign key book_id_fk (book_id) references books (book_id),
    foreign key user_id_fk (user_id) references users (user_id)
);

create table if not exists status_explain (
    status tinyint,
    status_name varchar(20)
);

create table if not exists b_r_explain (
    b_r tinyint,
    b_r_name varchar(20)
);