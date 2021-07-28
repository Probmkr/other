drop procedure if exists borrow_book;

delimiter //
create procedure borrow_book (in u_id int, in b_id int)
begin

insert into borrow_status (user_id, book_id) values (u_id, b_id);
insert into b_r_log (user_id, book_id, b_r) values (u_id, b_id, 1);

end
//

delimiter ;