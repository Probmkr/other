delimiter //
create trigger borrow on borrow_status for each row
begin
insert into b_r_log (user_id, book_id, b_r) values (
    new.user_id, new.book_id, 1
)