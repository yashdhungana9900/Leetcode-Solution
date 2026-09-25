class Solution(object):
    def equationsPossible(self, equations):
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA != rootB:
                parent[rootA] = rootB

        # Process all equalities first
        for eq in equations:
            if eq[1:3] == "==":
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                union(a, b)

        # Check inequalities
        for eq in equations:
            if eq[1:3] == "!=":
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')

                if find(a) == find(b):
                    return False

        return True