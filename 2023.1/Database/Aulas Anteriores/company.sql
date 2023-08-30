create database company2;
use company2;

create table employees(
	cpf bigint primary key,
    name varchar(150) not null,
    gender enum("M", "F") not null,
    bornDate date not null,
	hiringDate date not null
);

create table role(
	roleId bigint auto_increment primary key,
    cpf bigint not null,
    startDate date not null,
    endDate date,
    foreign key(cpf) references employees(cpf)
);

create table departaments(
	departamentId bigint auto_increment primary key,
    depName varchar(100) not null
);

create table manager(
	managerId bigint auto_increment primary key,
    departamentId bigint not null,
    cpf bigint not null,
    startDate date not null,
    endDate date,
    foreign key(cpf) references employees(cpf),
    foreign key(departamentId) references departaments(departamentId)
);

create table employeedep(
	id bigint auto_increment primary key,
    departamentId bigint not null,
    cpf bigint not null,
    enterDate date not null,
    exitDate date,
    foreign key(cpf) references employees(cpf),
    foreign key(departamentId) references departaments(departamentId)
);

create table salary(
	salaryId bigint auto_increment primary key,
    cpf bigint not null,
	value float not null,
    startDate date not null,
    endDate date,
    foreign key(cpf) references employees(cpf)
);