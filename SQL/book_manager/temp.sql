select book_name, author, date from books inner join lend_status using (book_id) where user_id = 1 and book_name like '%ccc%'