use test;
drop table if exists from_sql;
create table from_sql (
    id int,
    num int
);
insert into from_sql values (
    0,
    1
),(
    1,
    2
),(
    2,
    3
);
select * from from_sql;
