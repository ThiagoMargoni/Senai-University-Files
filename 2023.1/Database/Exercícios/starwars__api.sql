drop database if exists starwars;
create database starwars;
use starwars;

create table films(
	id bigint primary key auto_increment,
    name varchar(50) not null,
    description varchar(500) not null
);

create table chars (
	id bigint primary key auto_increment,
    name varchar(50) not null,
    description varchar(500) not null
);

create table starships(
	id bigint primary key auto_increment,
    name varchar(50) not null,
    model varchar(50) not null,
    manufacturer varchar(50) not null,
    cost_in_credits varchar(50) not null,
    length varchar(50) not null,
    max_atmosphering_speed varchar(50) not null,
    crew varchar(50) not null,
    passengers varchar(50) not null,
    cargo_capacity varchar(50) not null,
    consumables varchar(50) not null,
    hyperdrive_rating varchar(50) not null,
    MGLT varchar(50) not null,
    starship_class varchar(50) not null,
    created varchar(50) not null,
    edited varchar(50) not null,
    url varchar(150) not null
);

create table ships_films(
	id bigint primary key auto_increment,
    fk_filmId bigint not null,
    fk_shipId bigint not null,
    foreign key(fk_filmId) references films(id),
    foreign key(fk_shipId) references starships(id)
);

create table pilots (
	id bigint primary key auto_increment,
    fk_charId bigint not null,
    fk_shipId bigint not null,
    foreign key(fk_charId) references chars(id),
    foreign key(fk_shipId) references starships(id)
);