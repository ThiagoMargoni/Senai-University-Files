select count(*) from employees;
select count(*) from titles;
select count(*) from departments;
select count(*) from dept_manager;
select count(*) from dept_emp;
select count(*) from salaries;

select * from employees employees
inner join salary s on e.id = s.employeeFK
where s.amount in (
	select max(amount) from salary
);

select  e.emp_no, e.first_name, count(e.emp_no) number_titles from employees e
inner join salaries s on e.emp_no = s.emp_no
inner join titles t on e.emp_no = t.emp_no
group by e.emp_no;

select  e.emp_no, e.first_name, count(e.emp_no) number_titles from employees e
inner join salaries s on e.emp_no = s.emp_no
inner join titles t on e.emp_no = t.emp_no
group by e.emp_no having number_titles > 1;

select * from (
	select  e.emp_no, e.first_name, count(e.emp_no) number_titles from employees e
	inner join salaries s on e.emp_no = s.emp_no
	inner join titles t on e.emp_no = t.emp_no
	group by e.emp_no
) new_table where number_titles > 1;
