# Portfolio
SQL -Indian Census Data Analyst Project
1.CREATE NEW DATABASE

create database projects;
use projects;

2.iMPORT FILES 

SELECT * FROM projects.data1;

SELECT * FROM projects.data_2;
3.ANALYZING

#Number of rows in Dataset

select count(*) from projects.data1;

#Dataset for Kerala and Karnataka

select * from projects.data1 where State in ('Kerala','Karnataka');

#Population in India

select  sum(population) population from projects.data_2;

#Average Growth of India

select avg(Growth)*100 Avg_Growth from projects.data1;

#Average Growth of States

select State, avg(Growth)*100 Avg_Growth from projects.data1 group by State;

#Average Sex Ratio

select State,round(avg(Sex_Ratio),0) Avg_Sex_Ratio from projects.data1 group by State order by Avg_Sex_Ratio desc;

#Average Literacy rate above 90

select State,round(avg(Literacy),0) Avg_Literacy_Rate from projects.data1 group by State having round(avg(Literacy),0)>90 order by Avg_Literacy_Rate desc;

#Top 3 states with highest Growth rate

select state,avg(Growth)*100 Avg_Growth from projects.data1 group by state order by Avg_Growth desc limit 3;

#Bottom 3  states with lowest sex ratio 

select State,round(avg(Sex_Ratio),0) Avg_Sex_Ratio from projects.data1 group by State order by Avg_Sex_Ratio asc limit 3;

#Top and Bottom states in Literacy

drop table  if exists topstates;

create table topstates( state varchar(255),topstate float );

insert into topstates

select State,round(avg(Literacy),0) Avg_Literacy_Rate from projects.data1 group by State order by Avg_Literacy_Rate desc;

select  * from topstates order by topstates.topstate desc limit 3; 

drop table  if exists bottomstates;

create table bottomstates( state varchar(255),bottomstate float );

insert into bottomstates

select State,round(avg(Literacy),0) Avg_Literacy_Rate from projects.data1 group by State order by Avg_Literacy_Rate desc;

select  * from bottomstates order by bottomstates.bottomstate asc limit 3; 

#union of tables

select * from(
select  * from topstates order by topstates.topstate desc limit 3 )a
union
select * from (
select  * from bottomstates order by bottomstates.bottomstate asc limit 3)b;

#States with starting letter k amd a

select distinct state from projects.data1 where lower(state) like 'k%' or lower(state) like 'a%';

#States starts with letter a and ends with letter m

select distinct state from projects.data1 where lower(state) like 'a%' and lower(state) like '%m';

#Joining both tables

select a.district,a.state,a.sex_ratio,b.population from projects.data1 a inner join projects.data_2 b on a.district=b.district;

#Finding male ,female in each state

select c.district,c.state,round(c.population*c.sex_ratio/(100+c.sex_ratio),0) males,round((c.population * 100)/(100+c.sex_ratio),0) females from (
select a.district,a.state,a.sex_ratio ,b.population from projects.data1 a inner join projects.data_2 b on a.district=b.district)c;

#Total literacy rate

select c.district,c.state, (c.literacy_ratio * c.population) literate_people,((1-c.literacy_ratio)*c.population) illiterate_people from 
(select a.district,a.state,a.literacy literacy_ratio ,b.population from projects.data1 a inner join projects.data_2 b on a.district=b.district)c;
