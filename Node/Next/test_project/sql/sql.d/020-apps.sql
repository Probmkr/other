drop table if not exists apps;

create table apps (
  app_id int unsigned not null primary key auto_increment,
  app_name varchar(255) not null,
  display_name_ja varchar(255) not null,
  display_name_en varchar(255) not null,
  description_ja text not null,
  description_en text not null,
  url varchar(255) not null,
  created_at datetime not null default current_timestamp
);
