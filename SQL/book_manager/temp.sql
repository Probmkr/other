select book_name, author, status_name from books inner join status_explain using (status);