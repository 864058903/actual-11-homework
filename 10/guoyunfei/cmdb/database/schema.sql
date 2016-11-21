drop table if exists user;
create table user (
    id int primary key auto_increment,
    name varchar(32) not null,
    password varchar(32) not null,
    email varchar(32) not null default '',
    phone varchar(20) not null default ''
) engine=innodb default charset=utf8;


drop table if exists idc;
create table idc (
    id int primary key auto_increment,
    name varchar(32) not null,
    address varchar(32) not null default '',
    ip varchar(200) not null default '',
    status int not null default 0
) engine=innodb default charset=utf8;


drop table if exists asset;
create table asset (
    id int primary key auto_increment,
    sn varchar(125) not null unique key comment '资产标号',
    hostname varchar(64) comment '主机名',
    os varchar(64) comment '操作系统',
    ip varchar(256) comment 'ip地址',
    machine_room_id int comment '机房ID',
    vendor varchar(256) comment '生产厂商',
    model varchar(64) comment '型号',
    ram int comment '内存, 单位G',
    cpu int comment 'cpu核数',
    disk int comment '硬盘，单位G',
    time_on_shelves date comment '上架时间',
    over_guaranteed_date date comment '过保时间',
    business varchar(256) comment '业务',
    admin varchar(256) comment '使用者',
    status int default 0 comment '0正在使用, 1 维护, 2 删除'
) engine=innodb default charset=utf8;


drop table if exists monitor_host;
create table monitor_host(
    id int primary key auto_increment,
    ip varchar(128),
    cpu float,
    mem float,
    disk float,
    m_time datetime,
    r_time datetime
)engine=innodb default charset=utf8;