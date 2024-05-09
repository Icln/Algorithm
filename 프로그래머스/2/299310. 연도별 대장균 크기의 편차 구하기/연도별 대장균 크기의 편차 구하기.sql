with y as (
    select year(DIFFERENTIATION_DATE) as year, max(SIZE_OF_COLONY) as size
    from ECOLI_DATA
    group by year(DIFFERENTIATION_DATE)
)

select year(DIFFERENTIATION_DATE) as year, size - SIZE_OF_COLONY as YEAR_DEV, id
from ECOLI_DATA e join y on year(DIFFERENTIATION_DATE) = year
order by 1, 2