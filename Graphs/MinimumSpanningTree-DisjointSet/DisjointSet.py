# Disjoint Set
'''
Dynamic Graph -> 
Union -> Connects nodes

# Union (u, v)
1. Find ultimate parent of u & v: u => pu, v => pv
2. Find rank of pu and pv
3. Connect smaller rank to larger rank always
TC for Union = O(4 * Alpha) => O(1) as alpha is close to 1

# Path Compression -> Attaching the nodes to the ultimate parent
'''