SELECT count(id) as count
FROM ECOLI_DATA
WHERE GENOTYPE & 2 = 0 AND (GENOTYPE & 1 or GENOTYPE & 4)