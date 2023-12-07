-- CLASS ----------------------------
select * from #classbm
order by School,
		 case when Grade = 'K' then 0
			  when Grade = '6-8' then 9 
			  when Grade = '9-12' then 10
			  else Grade end,
		 Subject, Teacher, Class