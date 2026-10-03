# Write your MySQL query statement below
with Ad as
(select a.name As name , count(*) as count1 from Employee a inner join Employee e on a.id=e.managerId
group by a.id)
select name from Ad
where count1>=5


