-- using 549670077 as a seed to the RNG


select
	sum(l_extendedprice * l_discount) as revenue
from
	lineitem
where
	l_shipdate >= DATE '1997-01-01'
	and l_shipdate < DATE '1997-01-01' + INTERVAL '1 years'
	and l_discount between 0.03 - 0.01 and 0.03 + 0.01
	and l_quantity < 25;
