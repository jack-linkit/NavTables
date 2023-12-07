-- DISTRICT -------------------------
select Grade, Subject, max([Latest Results]) as [Latest Results],
sum([22-23 Form A]) as [22-23 Form A], sum([22-23 Form B]) as [22-23 Form B], sum([22-23 Form C]) as [22-23 Form C],
sum([23-24 Form A]) as [23-24 Form A], sum([23-24 Form B]) as [23-24 Form B], sum([23-24 Form C]) as [23-24 Form C]
from #bm
where ([22-23 Form A]+[22-23 Form B]+[22-23 Form C]+[23-24 Form A]+[23-24 Form B]+[23-24 Form C])>=0
group by Grade, Subject
order by case when Grade = 'K' then 0
			  when Grade = '6-8' then 9 
			  when Grade = '9-12' then 10
			  else Grade end,
		 Subject