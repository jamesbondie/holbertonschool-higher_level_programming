-- groups
select score, count(score) as number from second_table group by score order by score desc;
