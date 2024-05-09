with g as(
    select EMP_NO,
        case
            when avg(score) >= 96 then 'S'
            when avg(score) >= 90 then 'A'
            when avg(score) >= 80 then 'B'
            else 'C'
        end as grade
    from HR_GRADE
    WHERE YEAR = 2022
    GROUP BY EMP_NO, YEAR
), b as(
    select e.EMP_NO, EMP_NAME, grade,
        case grade
            when 'S' then sal * 20 / 100
            when 'A' then sal * 15 / 100
            when 'B' then sal * 10 / 100
            else 0
        end as bonus
    from HR_EMPLOYEES e join g on e.EMP_NO = g.EMP_NO 
)

select *
from b