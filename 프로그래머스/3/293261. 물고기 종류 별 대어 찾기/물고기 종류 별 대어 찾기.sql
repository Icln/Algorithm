select id, FISH_NAME, length
from FISH_INFO i join FISH_NAME_INFO n on i.fish_type = n.fish_type
where (fish_name, length) in
(   select FISH_NAME, max(LENGTH)
    from FISH_INFO i join FISH_NAME_INFO n on i.fish_type = n.fish_type
    group by FISH_NAME)