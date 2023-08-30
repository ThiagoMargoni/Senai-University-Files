create database email;
use email;

create table mail(
	mailId bigint auto_increment primary key,
	header varchar(100) not null,
    body varchar(1000),
    files text
);

create table recipients(
	emailRecipient varchar(100) primary key
);

create table mailSend(
	id bigint auto_increment primary key,
    mailId bigint not null,
	emailRecipient varchar(100) not null,
    status enum("rascunho", "enviado", "enviando") not null, 
    dateSend datetime not null,
    foreign key(mailId) references mail(mailId),
    foreign key(emailRecipient) references recipients(emailRecipient)
);