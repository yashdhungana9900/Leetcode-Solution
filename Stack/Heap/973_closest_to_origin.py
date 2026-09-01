import heapq

class Solution(object):
    def kClosest(self, points, k):

        heap = []

        for x, y in points:

            distance = x * x + y * y

            heapq.heappush(heap, (distance, x, y))

        result = []

        for _ in range(k):
            distance, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result