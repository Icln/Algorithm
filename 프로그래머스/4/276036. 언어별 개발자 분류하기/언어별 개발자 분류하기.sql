with fe as(
    select sum(code) as code
    from skillcodes
    group by category
    having category = "Front End"
), tmp as(
    SELECT ID, EMAIL,
        CASE
            WHEN d.SKILL_CODE & fe.code
                AND d.SKILL_CODE & (SELECT code FROM SKILLCODES WHERE NAME = 'Python')
                THEN 'A'
            WHEN d.SKILL_CODE & (SELECT code FROM SKILLCODES WHERE NAME = 'C#') 
                THEN 'B'
            WHEN d.SKILL_CODE & fe.code
                THEN 'C'
            ELSE NULL
        END AS GRADE
    FROM
        DEVELOPERS d, fe
)
select GRADE, ID, EMAIL
FROM tmp
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID