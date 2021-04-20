select * from books;

select * from users;

select * from b_r_log;

select * from borrow_status;

select * from status_explain;

select * from b_r_explain;

select user_name, book_name, author, date from borrow_status
    inner join books using (book_id)
    inner join users using (user_id);

select book_id, book_name, status_name from books
    inner join status_explain using (status)
    order by book_id;