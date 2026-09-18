class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False

            parent[rootA] = rootB
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []