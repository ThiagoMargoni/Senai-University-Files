/*create database warehouse;

use warehouse;*/

create table productlines(
	productLine varchar(50) primary key,
    textDescription varchar(150) not null,
    htmlDescription varchar(150) not null,
    image text not null
);

create table products(
	productCode bigint auto_increment primary key,
    productName varchar(50) not null,
    productLine varchar(50) not null,
    productScale bigint not null,
    productVendor varchar(100) not null,
    productDescription varchar(150) not null,
    quantityStock bigint not null,
    buyPrice float not null,
    msrp float not null,
    foreign key(productLine) references productlines(productLine)
);

create table customers(
	customerNumber bigint auto_increment primary key,
    customerName varchar(50) not null,
    contactLastName varchar(50) not null,
    contactFirstName varchar(50) not null,
    phone bigint not null,
    adressLine1 varchar(250) not null,
    adressLine2 varchar(250) not null,
    city varchar(50) not null,
    state varchar(50) not null,
    postalCode int not null,
    country varchar(50) not null,
    salesRep bigint not null,
    creditsLimit float not null
);

create table orders(
	orderNumber bigint auto_increment primary key,
    orderDate date not null,
    requiredDate date not null,
    shippedDate date not null,
    status varchar(50) not null,
    comments varchar(150) not null,
    customerNumber bigint not null,
    foreign key(customerNumber) references customers(customerNumber)
);

create table orderdetails(
	id bigint auto_increment primary key,
    orderNumber bigint not null,
    productCode bigint not null,
    quantityOrdered int not null,
    priceEach float not null,
    orderLineNumber int not null,
    foreign key(orderNumber) references orders(orderNumber),
    foreign key(productCode) references products(productCode)
);

create table offices (
	officeCode int primary key,
    city varchar(50) not null,
    phone int not null,
    adressLine1 varchar(250) not null,
    adressLine2 varchar(250) not null,
    state varchar(50) not null,
    postalCode int not null,
    country varchar(50) not null,
    territory varchar(50) not null
);

create table employees(
	employeeNumber bigint auto_increment primary key,
    lastName varchar(50) not null,
    firstName varchar(50) not null,
    extension varchar(50) not null,
    email varchar(100) not null,
    officeCode int not null,
    reportsTo varchar(100) not null,
    jobTitle varchar(50) not null,
    foreign key(officeCode) references offices(officeCode)
);

create table payments(
	checkNumber bigint auto_increment primary key,
	customerNumber bigint not null,
    paymenyDate date not null,
    amount float not null,
    foreign key(customerNumber) references customers(customerNumber)
);