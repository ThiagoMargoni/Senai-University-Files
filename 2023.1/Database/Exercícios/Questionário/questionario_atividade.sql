create database HogwartsUniversity;
use HogwartsUniversity;

create table Users(
	peopleIdentification varchar(50) primary key,
    userType varchar(15) default '---',
    course varchar(50) default '---',
    class varchar(15) default '---',
	period varchar(15) default '---'
);

insert into Users values('Anonymous', null, null, null, null);
insert into Users values('TDMNADS', 'Aluno', 'ADS', '1', 'Noite');
insert into Users values('RRDSNADS', 'Aluno', 'ADS', '1', 'Noite');
insert into Users values('ASNADS', 'Professor', 'ADS', null, null);
insert into Users values('SDSASRM', 'Diretor', null, null, null);

create table Survey(
	surveyId int primary key auto_increment,
    surveyName varchar(50) not null
);

insert into Survey values(0, 'Feedback Curso');

create table Answers(
	answerId int primary key auto_increment,
    surveyId int not null,
    answerDate datetime not null default now(),
    peopleIdentification varchar(150) default 'Anonymous',
    comments varchar(500),
    foreign key(surveyId) references Survey(surveyId),
    foreign key(peopleIdentification) references Users(peopleIdentification)
);

insert into Answers values(0, 1, '2023-05-10', null, 'Nothing to point');
insert into answers values(0, 1, '2023-05-10', 'TDMNADS', 'Good Course');
insert into answers values(0, 1, '2023-05-10', 'RRDSNADS', 'Bad Course');

create table QuestionsAnswers(
	id int primary key auto_increment,
    answerId int not null,
    question varchar(150) not null,
    importanceLvl enum('Alta', 'Média', 'Baixa') not null,
    satisfactionLvl enum('Ruim', 'Regular', 'Bom', 'Ótimo', 'NA') not null,
    foreign key(answerId) references answers(answerId)
);

insert into questionsanswers values(0, 1, 'Question 1', 'Alta', 'Ruim');
insert into questionsanswers values(0, 1, 'Question 2', 'Baixa', 'Bom');

insert into questionsanswers values(0, 2, 'Question 1', 'Alta', 'Ruim');
insert into questionsanswers values(0, 2, 'Question 2', 'Média', 'Ruim');

insert into questionsanswers values(0, 3, 'Question 1', 'Média', 'Regular');
insert into questionsanswers values(0, 3, 'Question 2', 'Média', 'Ótimo');

/* a */ select u.course, u.class Turma, count(a.answerId) TotalFormularios from answers a
inner join users u on a.peopleIdentification = u.peopleIdentification
group by u.course, u.class;

/* b */ select question, satisfactionLvl, count(satisfactionLvl) countRespostas from questionsanswers 
where satisfactionLvl = 'Ruim'
group by question 
order by countRespostas DESC limit 1;

/* c */ select question, satisfactionLvl, count(satisfactionLvl) countRespostas from questionsanswers 
where satisfactionLvl = 'Ótimo'
group by question 
order by countRespostas DESC limit 1;

/* d */ select u.course, u.class, q.question, q.satisfactionLvl, count(q.satisfactionLvl) countRespostas from questionsanswers q
inner join answers a on a.answerId = q.answerId
inner join users u on u.peopleIdentification = a.peopleIdentification
where satisfactionLvl = 'Ruim'
group by u.course, u.class, q.question 
order by countRespostas DESC limit 1;

/* e */ select u.course, u.class, q.question, q.satisfactionLvl, count(q.satisfactionLvl) countRespostas from questionsanswers q
inner join answers a on a.answerId = q.answerId
inner join users u on u.peopleIdentification = a.peopleIdentification
where satisfactionLvl = 'Ótimo'
group by u.course, u.class, q.question 
order by countRespostas DESC limit 1;

/* f */ select question, importanceLvl, count(importanceLvl) countRespostas from questionsanswers 
where importanceLvl = 'Alta'
group by question 
order by countRespostas DESC limit 1;

/* g */ select question, importanceLvl, count(importanceLvl) countRespostas from questionsanswers 
where importanceLvl = 'Baixa'
group by question 
order by countRespostas DESC limit 1;

/* h */ select u.course, u.class, q.question, q.importanceLvl, count(q.importanceLvl) countRespostas from questionsanswers q
inner join answers a on a.answerId = q.answerId
inner join users u on u.peopleIdentification = a.peopleIdentification
where importanceLvl = 'Alta'
group by u.course, u.class, q.question 
order by countRespostas DESC limit 1;

/* i */ select u.course, u.class, q.question, q.importanceLvl, count(q.importanceLvl) countRespostas from questionsanswers q
inner join answers a on a.answerId = q.answerId
inner join users u on u.peopleIdentification = a.peopleIdentification
where importanceLvl = 'Baixa'
group by u.course, u.class, q.question 
order by countRespostas DESC limit 1;

/* j */ select u.course, u.class Turma, count(a.answerId) TotalFormularios from answers a
inner join users u on a.peopleIdentification = u.peopleIdentification
group by u.course, u.class
order by TotalFormularios desc limit 1; 

select u.course, u.class Turma, count(a.answerId) TotalFormularios from answers a
inner join users u on a.peopleIdentification = u.peopleIdentification
group by u.course, u.class
order by TotalFormularios asc limit 1; 