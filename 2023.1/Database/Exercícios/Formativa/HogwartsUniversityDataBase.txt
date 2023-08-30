create database HogwartsUniversity;
use HogwartsUniversity;

create table Roles(
	roleId int primary key auto_increment,
    roleName varchar(50) not null,
    description varchar(150) not null
);

create table AccessRole(
	id int primary key auto_increment,
    accessLevel varchar(20) not null,
    roleId int not null,
    foreign key(roleId) references Roles(roleId)
);

create table Users(
	userId int primary key auto_increment,
    status enum('a', 'i') not null,
    accessRoleId int not null,
    name varchar(150) not null,
    email varchar(150) not null,
    password varchar(50) not null,
    bornDate date not null,
    registerDate datetime not null default now(),
    foreign key(accessRoleId) references AccessRole(id)
);

create table Places(
	placeId int primary key auto_increment,
    placeName varchar(50) not null,
    universityBloc varchar(1) not null,
    maxPeople int not null
);

create table Inventory (
	inventoryId int primary key auto_increment,
    itemName varchar(50) not null,
    description varchar(150) not null
);

create table CheckList(
	id int primary key auto_increment,
    placeId int not null,
    inventoryId int not null,
    onPlace bool not null,
    foreign key(placeId) references Places(placeId),
    foreign key(inventoryId) references Inventory(inventoryId)
);

create table Events(
	eventId int primary key auto_increment,
    placeId int not null,
    eventName varchar(50) not null,
    startDate datetime not null,
    endDate datetime not null,
    checkInMaxDate datetime not null,
    checkInMinDate datetime not null,
    quantityAvailable int not null,
    foreign key(placeId) references Places(placeId)
);

create table UserEvent(
	id int primary key auto_increment,
	eventId int not null,
    userId int not null,
    checkInDate datetime not null,
    foreign key(eventId) references Events(eventId),
    foreign key(userId) references Users(userId)
);