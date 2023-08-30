select * from employees as e
join salary as s on e.cpf = s.cpf
where s.amount > 5000;

select max(amount) from salary;

select * from employees as e
join salary as s on e.cpf = s.cpf
where s.amount in (
	select max(amount) from salary
);

select * from employees as e
join employeedep as de on de.cpf = e.cpf
join departaments as d on d.departamentId = de.departamentId
join manager as m on m.departamentId = d.departamentId
where m.cpf = 4;

select * from role as r
join employees as e on e.cpf = r.cpf
where e.name = 'Maria';

select amount from salary group by salary;