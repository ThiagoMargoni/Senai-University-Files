select customerName, phone from customers;

select * from customers where country = 'USA' and (city = 'Las Vegas' or city = 'San Francisco');

select * from customers where country = "France" and creditLimit > 5000;

select * from customers where customerName like "A%";

select * from customers as c
join employees as e on c.salesRepEmployeeNumber = e.employeeNumber
join offices as o on o.officeCode = e.officeCode
join payments as p on p.customerNumber = c.customerNumber
join orders as od on od.customerNumber = c.customerNumber
join orderdetails as odt on odt.orderNumber = od.orderNumber
join products as pr on pr.productCode = odt.productCode
join productlines as pl on pl.productLine = pr.productLine;

select * from orders as o
join orderdetails as od on o.orderNumber = od.orderNumber
join products as p on p.productCode = od.productCode
where p.productCode = 'S12_3891';

select count(*) from customers;
select count(*) from offices;

select country from customers group by country having country like 'a%' order by country asc;

select c.customerNumber, count(*) as total 
from customers as c 
join orders as o on c.customerNumber = o.customerNumber
group by c.customerName having total > 1
order by c.customerName asc;