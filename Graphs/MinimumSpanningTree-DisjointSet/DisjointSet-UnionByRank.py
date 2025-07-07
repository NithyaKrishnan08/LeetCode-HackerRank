# Disjoint set - Union By Rank

# TimeComplexity
# findParent: O(1)
# unionByRank: O(1)
# Space Complexity: O(N)
class DisjointSet:
  def __init__(self, n):
    self.rank = [0] * (n + 1)
    self.size = [1] * (n + 1)
    self.parent = [i for i in range(n+1)]

  def findParent(self, node):
    if node == self.parent[node]:
      return node
    
    # Path compression
    self.parent[node] = self.findParent(self.parent[node])
    
    return self.parent[node]
  
  def unionByRank(self, u, v):
    ultParent_u = self.findParent(u)
    ultParent_v = self.findParent(v)

    if ultParent_u == ultParent_v:
      return
    
    if self.rank[ultParent_u] < self.rank[ultParent_v]:
      self.parent[ultParent_u] = ultParent_v
    elif self.rank[ultParent_v] < self.rank[ultParent_u]:
      self.parent[ultParent_v] = ultParent_u
    else:
      self.parent[ultParent_v] = ultParent_u
      self.rank[ultParent_u] += 1

  def unionBySize(self, u, v):
    ultParent_u = self.findParent(u)
    ultParent_v = self.findParent(v)

    if ultParent_u == ultParent_v:
      return
    
    if self.size[ultParent_u] < self.size[ultParent_v]:
      self.parent[ultParent_u] = ultParent_v
      self.size[ultParent_v] += self.size[ultParent_u]
    else:
      self.parent[ultParent_v] = ultParent_u
      self.size[ultParent_u] += self.size[ultParent_v]

if __name__ == "__main__":
  ds = DisjointSet(7)
  ds.unionBySize(1, 2)
  ds.unionBySize(2, 3)
  ds.unionBySize(4, 5)
  ds.unionBySize(6, 7)
  ds.unionBySize(5, 6)
  # If 3 and 7 belong to the same component
  if ds.findParent(3) == ds.findParent(7):
    print(f"3 and 7 belong to the same component")
  else:
    print(f"3 and 7 does not belong to the same component")
  ds.unionBySize(3, 7)
  if ds.findParent(3) == ds.findParent(7):
    print(f"3 and 7 belong to the same component")
  else:
    print(f"3 and 7 does not belong to the same component")


