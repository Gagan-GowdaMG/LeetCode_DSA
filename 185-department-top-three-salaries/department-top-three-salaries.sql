# Write your MySQL query statement below
with high as(select d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        DENSE_RANK() over (partition by  d.name order by e.salary desc) as ranq
        from Employee e  join Department d
        on e.departmentId=d.id)
select Department,Employee,Salary from high
where ranq <=3;
