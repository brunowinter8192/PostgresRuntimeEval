-- using 992687751 as a seed to the RNG


select
	o_orderpriority,
	count(*) as order_count
from
	orders
where
	o_orderdate >= DATE '1996-06-01'
	and o_orderdate < DATE '1996-06-01' + INTERVAL '3 months'
	and exists (
		select
			*
		from
			lineitem
		where
			l_orderkey = o_orderkey
			and l_commitdate < l_receiptdate
	)
group by
	o_orderpriority
order by
	o_orderpriority;
