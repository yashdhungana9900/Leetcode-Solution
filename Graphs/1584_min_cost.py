class Solution(object):
    def minCostConnectPoints(self, points):
        n = len(points)

        visited = [False] * n
        min_dist = [float('inf')] * n

        min_dist[0] = 0
        total = 0

        for _ in range(n):
            # Find unvisited point with minimum distance
            curr = -1

            for i in range(n):
                if not visited[i] and (curr == -1 or min_dist[i] < min_dist[curr]):
                    curr = i

            visited[curr] = True
            total += min_dist[curr]

            # Update distances
            for i in range(n):
                if not visited[i]:
                    distance = (
                        abs(points[curr][0] - points[i][0]) +
                        abs(points[curr][1] - points[i][1])
                    )

                    min_dist[i] = min(min_dist[i], distance)

        return total