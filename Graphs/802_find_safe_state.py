class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        state = [0] * n
        # 0 = unvisited
        # 1 = visiting
        # 2 = safe

        def dfs(node):
            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            state[node] = 1

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            state[node] = 2
            return True

        result = []

        for node in range(n):
            if dfs(node):
                result.append(node)

        return result
        