class Solution(object):
    def gardenNoAdj(self, n, paths):
        graph = [[] for _ in range(n)]

        for a, b in paths:
            a -= 1
            b -= 1

            graph[a].append(b)
            graph[b].append(a)

        color = [0] * n

        for garden in range(n):
            used = set()

            for neighbor in graph[garden]:
                if color[neighbor]:
                    used.add(color[neighbor])

            for flower in range(1, 5):
                if flower not in used:
                    color[garden] = flower
                    break

        return color