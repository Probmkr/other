drop procedure if exists borrow_book;

delimiter //
create procedure borrow_book (in u_id int, in b_id int)
begin

update books set status = 2 where book_id = b_id;
insert into borrow_status (user_id, book_id) values (u_id, b_id);
insert into b_r_log (user_id, book_id, b_r) values (u_id, b_id, 1);

end
//

delimiter ;

drop procedure if exists return_book;

delimiter //
create procedure return_book (in u_id int, in b_id int)
begin

update books set status = 1 where book_id = b_id;
delete from borrow_status where user_id = u_id and book_id = b_id;
insert into b_r_log (user_id, book_id, b_r) values (u_id, b_id, 2);

end
//

delimiter ;