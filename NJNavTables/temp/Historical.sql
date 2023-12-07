-- HISTORICAL -----------------------
select Grade, Subject, 
sum([19-20 Form A]) as [19-20 A], sum([19-20 Form B]) as [19-20 B], sum([19-20 Form C]) as [19-20 C],
sum([20-21 Form A]) as [20-21 A], sum([20-21 Form B]) as [20-21 B], sum([20-21 Form C]) as [20-21 C],
sum([21-22 Form A]) as [21-22 A], sum([21-22 Form B]) as [21-22 B], sum([21-22 Form C]) as [21-22 C],
sum([22-23 Form A]) as [22-23 A], sum([22-23 Form B]) as [22-23 B], sum([22-23 Form C]) as [22-23 C],
sum([23-24 Form A]) as [23-24 A], sum([23-24 Form B]) as [23-24 B], sum([23-24 Form C]) as [23-24 C]
from #bm
group by Grade, Subject
order by case when Grade = 'K' then 0
			  when Grade = '6-8' then 9 
			  when Grade = '9-12' then 10
			  else Grade end,
		 Subject
