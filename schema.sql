drop table if exists rate;
    create table rate (
    id integer primary key autoincrement,
    comment text,
    id_course integer,
    id_user integer,
    rate integer,
    time_added time
);