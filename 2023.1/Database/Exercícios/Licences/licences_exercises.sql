/*a)*/ select count(*) from lcliente;

/*b)*/ select * from llicenca where month(DtAquisicao) = 09;

/*c)*/ select * from llicenca where month(DtAquisicao) = 05 and year(DtAquisicao) = 2007;

/*d)*/ select *, substring(descricao, 1, 5) iniciais_desc from ltipo_empresa order by descricao desc;

/*e)*/ select *, substring(descricao, length(descricao)-4, 5) iniciais_desc from ltipo_empresa order by descricao desc;

/*f)*/ select *, substring(descricao, 6, 10) iniciais_desc from ltipo_empresa;

/*g)*/ select Nome_RazaoSocial, length(Nome_RazaoSocial) bytes_nome from lcliente order by Nome_RazaoSocial;

/*h)*/ select NumLicenca, DtAquisicao, DATEDIFF(now(), DtAquisicao)  from llicenca; 

/*i)*/ select upper(NomeSetor) Maiusculo, lower(NomeSetor) Minusculo from lsetor;

/*j)*/ select s.NomeSoftware, v.Versao from lsoftware s
inner join lversao v on v.idSOFTWARE_FK = idSOFTWARE
group by s.NomeSoftware, v.Versao;

/*k)*/ select te.descricao, s.NomeSetor from lcliente c
inner join ltipo_empresa te on c.idTIPO_Empresa_FK = te.idTIPO_Empresa
inner join lsetor s on c.idSETOR_FK = s.idSETOR
group by te.descricao, s.NomeSetor;

/*l)*/ select c.idCLIENTE, c.Nome_RazaoSocial, l.NumLicenca, l.DtAquisicao, l.ValorAquisicao from llicenca l
inner join lcliente c on l.idCLIENTE_FK = c.idCLIENTE;

/*m)*/ select distinct c.Nome_RazaoSocial, s.NomeSoftware from llicenca l
inner join lcliente c on c.idCLIENTE = l.idCLIENTE_FK
inner join lsoftware s on s.idSOFTWARE = l.idSOFTWARE_FK_FK
group by c.Nome_RazaoSocial, s.NomeSoftware;

/*n)*/ select c.Nome_RazaoSocial, te.descricao, s.NomeSetor from lcliente c
inner join ltipo_empresa te on c.idTIPO_Empresa_FK = te.idTIPO_Empresa
inner join lsetor s on c.idSETOR_FK = s.idSETOR
where c.UF in ('SP', 'RS', 'PR', 'MG');

/*o)*/ select so.nomesoftware, l.versao_fk, c.nome_razaosocial, e.descricao, s.nomesetor, l.dtaquisicao, l.valoraquisicao
from lcliente c
inner join ltipo_empresa e on c.idtipo_empresa_fk = e.idtipo_empresa
inner join lsetor s on c.idsetor_fk = s.idsetor
inner join llicenca l on l.idcliente_fk = c.idcliente
inner join lsoftware so on l.idsoftware_fk_fk = so.idsoftware
order by so.nomesoftware, l.versao_fk, l.dtaquisicao, c.nome_razaosocial;

/*p)*/ select count(*) quantidade_vendida from llicenca;

/*q)*/ select sum(valoraquisicao) valor_total, avg(valoraquisicao) media_valores, min(valoraquisicao) menor_valor, max(valoraquisicao) maior_valor from llicenca;

/*r)*/ select count(s.nomesetor) 
from lcliente c
inner join lsetor s on c.idsetor_fk = s.idsetor
where s.nomesetor = 'Farmacautica';

/*s)*/ select c.nome_razaosocial, count(l.idCLIENTE_FK) quantidade_comprada
from lcliente c
inner join llicenca l on l.idcliente_fk = c.idcliente
group by l.idCLIENTE_FK
order by c.nome_razaosocial;

/*t)*/ select c.nome_razaosocial, count(l.idcliente_fk) quantidade_comprada, sum(l.valoraquisicao) soma_valor_cliente, avg(l.valoraquisicao) media_valor_cliente
from lcliente c
inner join llicenca l on l.idcliente_fk = c.idcliente
group by l.idCLIENTE_FK
order by c.nome_razaosocial;

/*u)*/ select s.nomesetor, sum(l.valoraquisicao)
from lsetor s
inner join lcliente c on c.idsetor_fk = s.idsetor 
inner join llicenca l on l.idcliente_fk = c.idcliente
group by c.idsetor_fk
order by s.nomesetor;

/*v)*/ select te.descricao, sum(l.valoraquisicao)
from ltipo_empresa te
inner join lcliente c on c.idtipo_empresa_fk = te.idtipo_empresa 
inner join llicenca l on l.idcliente_fk = c.idcliente
group by c.idtipo_empresa_fk
order by te.idtipo_empresa;

/*w)*/ select s.nomesoftware, v.versao,sum(l.valoraquisicao)
from llicenca l
inner join lversao v on l.versao_fk = v.versao
inner join lsoftware s on l.idsoftware_fk_fk = s.idsoftware
group by l.idsoftware_fk_fk, l.versao_fk
order by l.idsoftware_fk_fk, l.versao_fk;

/*x)*/ select s.nomesoftware, c.nome_razaosocial, count(l.idsoftware_fk_fk) total_licencas_software
from lcliente c
inner join llicenca l on l.idcliente_fk = c.idcliente
inner join lsoftware s on l.idsoftware_fk_fk = s.idsoftware
group by l.idcliente_fk, l.idsoftware_fk_fk
order by c.nome_razaosocial;

/*y)*/ select * from
(select c.nome_razaosocial, count(l.idCLIENTE_FK) quantidade_comprada
from lcliente c
inner join llicenca l on l.idcliente_fk = c.idcliente
group by l.idCLIENTE_FK
order by c.nome_razaosocial) tabela
where quantidade_comprada > 10;