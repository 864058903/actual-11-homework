drop table if exists user;
create table user (
    id int primary key auto_increment,
    name varchar(32) not null,
    password varchar(32) not null,
    email varchar(32) not null default '',
    phone varchar(20) not null default ''
);

drop table if exists idc;
create table idc (
    id int primary key auto_increment,
    name varchar(32) not null,
    address varchar(32) not null default '',
    ip varchar(200) not null default '',
    status int not null default 0
);
