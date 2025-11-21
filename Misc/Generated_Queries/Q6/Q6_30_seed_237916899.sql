-- using 237916899 as a seed to the RNG


select
	sum(l_extendedprice * l_discount) as revenue
from
	lineitem
where
	l_shipdate >= DATE '1994-01-01'
	and l_shipdate < DATE '1994-01-01' + INTERVAL '1 years'
	and l_discount between 0.04 - 0.01 and 0.04 + 0.01
	and l_quantity < 24;
