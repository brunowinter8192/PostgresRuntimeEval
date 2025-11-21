import pandas as pd

def build_children_map(query_ops):
    children_map = {}
    
    for idx in range(len(query_ops)):
        current_row = query_ops.iloc[idx]
        current_depth = current_row['depth']
        current_node_id = current_row['node_id']
        
        children = []
        
        for j in range(idx + 1, len(query_ops)):
            next_row = query_ops.iloc[j]
            
            if next_row['depth'] == current_depth + 1:
                children.append({
                    'node_id': next_row['node_id'],
                    'node_type': next_row['node_type'],
                    'relationship': next_row['parent_relationship']
                })
            elif next_row['depth'] <= current_depth:
                break
        
        children_map[current_node_id] = children
    
    return children_map

df = pd.read_csv('operator_dataset_20251102_140747.csv', delimiter=';')
q8_100 = df[df['query_file'] == 'Q8_100_seed_812199069'].copy()

print(f"Total operators: {len(q8_100)}")
print("\nOperator structure:")
for idx, row in q8_100.iterrows():
    indent = "  " * row['depth']
    print(f"{indent}[{row['depth']}] {row['node_id']}: {row['node_type']} ({row['parent_relationship']})")

children_map = build_children_map(q8_100)

print("\n\nChildren Map:")
for node_id, children in children_map.items():
    if children:
        print(f"\nNode {node_id}:")
        for child in children:
            print(f"  -> {child['node_id']}: {child['node_type']} ({child['relationship']})")
