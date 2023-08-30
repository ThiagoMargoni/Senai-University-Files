/*ENUM() = opções limitadas*/

CREATE DATABASE tdm;

USE tdm;

DROP DATABASE tdm;

CREATE TABLE Employees (
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    employee_number BIGINT NOT NULL, 
    hired_date DATE NOT NULL, 
    department VARCHAR(20) NOT NULL
);

SHOW DATABASES;

SHOW TABLES;

SELECT * FROM Employees;

DROP TABLE Employees;

CREATE TABLE Employees (
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    employee_number BIGINT NOT NULL, 
    hired_date DATE NOT NULL, 
    department_id BIGINT NOT NULL,
    FOREIGN KEY(department_id) REFERENCES Departments(id)
);

CREATE TABLE Departments (
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
    depart VARCHAR(15) NOT NULL,
    manager VARCHAR(100) NOT NULL 
);

DESCRIBE Employees;

ALTER TABLE Employees MODIFY name VARCHAR(101) NOT NULL;

CREATE TABLE Funcionario (
	codFunc BIGINT AUTO_INCREMENT PRIMARY KEY,
    nomeFunc VARCHAR(45) NOT NULL
);

CREATE TABLE PEDIDO (
	numPedido BIGINT AUTO_INCREMENT PRIMARY KEY, 
	dataPedido DATETIME NOT NULL,
    valorTotal NUMERIC(10, 2), 
    codFunc_fk BIGINT NOT NULL,
    FOREIGN KEY(codFunc_fk) REFERENCES Funcionario(codFunc)
);