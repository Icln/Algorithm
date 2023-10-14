select i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
from animal_ins as i join animal_outs as o
    on i.animal_id = o.animal_id
where i.animal_id not in (
        select animal_id
        from animal_ins
        where sex_upon_intake LIKE 'Spayed%' or 
        sex_upon_intake LIKE 'Neutered%')
      and (o.sex_upon_outcome LIKE 'Neutered%' or
           o.sex_upon_outcome LIKE 'Spayed%')
order by i.animal_id