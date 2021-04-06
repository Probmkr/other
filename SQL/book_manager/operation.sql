insert into status_explain values (
    -1, 'cant use'
), (
    0, 'unknown'
), (
    1, 'can borrow'
), (
    2, 'be borrowed'
);

insert into l_r_explain values (
    1, 'borrow'
), (
    2, 'return'
);

insert into users (user_name, password, birthday) values (
    'root', 'IamRootUser', null
), (
    'Thanatos', 'thanat9191', null
);

insert into books (book_name, author, price, status) values (
    'aaa', 'aaaa', 100, 1
), (
    'bbb', 'aaaa', 100, 1
), (
    'ccc', 'bbbb', 200, 1
), (
    'ddd', 'bbbb', 200, 1
);

insert into lend_status (user_id, book_id) values (
    1, 3
), (
    2, 1
);

update books set status = 2 where book_id in (
    select book_id from lend_status
);

insert into l_r_log (user_id, book_id, l_r) values (
    1, 3, 1
), (
    2, 1, 1
);