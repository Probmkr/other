select * from books;

select * from users;

select * from l_r_log;

select * from lend_status;

select * from status_explain;

select * from l_r_explain;

select user_name, book_name, author, date from lend_status
    inner join books using (book_id)
    inner join users using (user_id);

select book_id, book_name, status_name from books
    inner join status_explain using (status)
    order by book_id;