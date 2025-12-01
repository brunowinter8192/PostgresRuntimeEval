# Debug: Original Script Pattern Prediction

Pattern: Hash Join -> [Seq Scan (Outer), Hash (Inner)]
Pattern Hash: 895c6e8c1a30a094329d71cef3111fbd
Pattern Length: 2

Model Features (exec): ['HashJoin_total_cost', 'Hash_Inner_rt1', 'Hash_Inner_rt2', 'Hash_Inner_st1', 'Hash_Inner_st2', 'SeqScan_Outer_np', 'SeqScan_Outer_rt1', 'SeqScan_Outer_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_st2']
Model Features (start): ['HashJoin_nt', 'HashJoin_sel', 'Hash_Inner_rt1', 'Hash_Inner_rt2', 'Hash_Inner_st1', 'Hash_Inner_st2', 'SeqScan_Outer_rt1', 'SeqScan_Outer_rt2', 'SeqScan_Outer_st1', 'SeqScan_Outer_st2']


## Query: Q3_100_seed_812199069


### Pattern Match at Hash Join (node_id 4356, depth 5)
Pattern nodes: [4356, 4357, 4358]
Cache before pattern: [4359, 4357, 4358]

Processing Hash Join (id 4356), prefix=HashJoin_
  Full children of 4356: [np.int64(4357), np.int64(4358)]
    Child 4357: in_pattern=True, in_cache=True, rel=Outer
    Child 4358: in_pattern=True, in_cache=True, rel=Inner

Processing Seq Scan (id 4357), prefix=SeqScan_Outer_
  Full children of 4357: []

Processing Hash (id 4358), prefix=Hash_Inner_
  Full children of 4358: [np.int64(4359)]
    Child 4359: in_pattern=False, in_cache=True, rel=Outer
      -> Set Hash_Inner_st1=0.3183, Hash_Inner_rt1=30.0995

Aggregated features:
  HashJoin_total_cost: 37331.91
  Hash_Inner_rt1: 30.099473810047385
  Hash_Inner_rt2: 0.0
  Hash_Inner_st1: 0.31825077450749695
  Hash_Inner_st2: 0.0
  SeqScan_Outer_np: 26136
  SeqScan_Outer_rt1: 0.0
  SeqScan_Outer_rt2: 0.0
  SeqScan_Outer_st1: 0.0
  SeqScan_Outer_st2: 0.0

Prediction: exec=498.5752, start=14.7733

## Query: Q5_107_seed_869627286


### Pattern Match at Hash Join (node_id 7054, depth 11)
Pattern nodes: [7054, 7055, 7056]
Cache before pattern: [7057, 7055, 7056]

Processing Hash Join (id 7054), prefix=HashJoin_
  Full children of 7054: [np.int64(7055), np.int64(7056)]
    Child 7055: in_pattern=True, in_cache=True, rel=Outer
    Child 7056: in_pattern=True, in_cache=True, rel=Inner

Processing Seq Scan (id 7055), prefix=SeqScan_Outer_
  Full children of 7055: []

Processing Hash (id 7056), prefix=Hash_Inner_
  Full children of 7056: [np.int64(7057)]
    Child 7057: in_pattern=False, in_cache=True, rel=Outer
      -> Set Hash_Inner_st1=0.0519, Hash_Inner_rt1=13.0796

Aggregated features:
  HashJoin_total_cost: 2.4
  Hash_Inner_rt1: 13.079574437254479
  Hash_Inner_rt2: 0.0
  Hash_Inner_st1: 0.05186146210476378
  Hash_Inner_st2: 0.0
  SeqScan_Outer_np: 1
  SeqScan_Outer_rt1: 0.0
  SeqScan_Outer_rt2: 0.0
  SeqScan_Outer_st1: 0.0
  SeqScan_Outer_st2: 0.0

Prediction: exec=498.5752, start=14.7733

### Pattern Match at Hash Join (node_id 7051, depth 9)
Pattern nodes: [7051, 7052, 7053]
Cache before pattern: [7057, 7055, 7056, 7054, 7052, 7053]

Processing Hash Join (id 7051), prefix=HashJoin_
  Full children of 7051: [np.int64(7052), np.int64(7053)]
    Child 7052: in_pattern=True, in_cache=True, rel=Outer
    Child 7053: in_pattern=True, in_cache=True, rel=Inner

Processing Seq Scan (id 7052), prefix=SeqScan_Outer_
  Full children of 7052: []

Processing Hash (id 7053), prefix=Hash_Inner_
  Full children of 7053: [np.int64(7054)]
    Child 7054: in_pattern=False, in_cache=True, rel=Outer
      -> Set Hash_Inner_st1=14.7733, Hash_Inner_rt1=498.5752

Aggregated features:
  HashJoin_total_cost: 4586.84
  Hash_Inner_rt1: 498.575158082332
  Hash_Inner_rt2: 0.0
  Hash_Inner_st1: 14.77334882684627
  Hash_Inner_st2: 0.0
  SeqScan_Outer_np: 3600
  SeqScan_Outer_rt1: 0.0
  SeqScan_Outer_rt2: 0.0
  SeqScan_Outer_st1: 0.0
  SeqScan_Outer_st2: 0.0

Prediction: exec=498.5752, start=14.7733

### Pattern Match at Hash Join (node_id 7048, depth 7)
Pattern nodes: [7048, 7049, 7050]
Cache before pattern: [7057, 7055, 7056, 7054, 7052, 7053, 7051, 7049, 7050]

Processing Hash Join (id 7048), prefix=HashJoin_
  Full children of 7048: [np.int64(7049), np.int64(7050)]
    Child 7049: in_pattern=True, in_cache=True, rel=Outer
    Child 7050: in_pattern=True, in_cache=True, rel=Inner

Processing Seq Scan (id 7049), prefix=SeqScan_Outer_
  Full children of 7049: []

Processing Hash (id 7050), prefix=Hash_Inner_
  Full children of 7050: [np.int64(7051)]
    Child 7051: in_pattern=False, in_cache=True, rel=Outer
      -> Set Hash_Inner_st1=14.7733, Hash_Inner_rt1=498.5752

Aggregated features:
  HashJoin_total_cost: 38475.32
  Hash_Inner_rt1: 498.575158082332
  Hash_Inner_rt2: 0.0
  Hash_Inner_st1: 14.77334882684627
  Hash_Inner_st2: 0.0
  SeqScan_Outer_np: 26136
  SeqScan_Outer_rt1: 0.0
  SeqScan_Outer_rt2: 0.0
  SeqScan_Outer_st1: 0.0
  SeqScan_Outer_st2: 0.0

Prediction: exec=498.5752, start=14.7733