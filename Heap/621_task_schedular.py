import heapq
from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        count = Counter(tasks)

        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)

        time = 0

        while heap:
            temp = []
            cycle = n + 1

            while cycle > 0 and heap:
                freq = -heapq.heappop(heap)
                freq -= 1

                if freq > 0:
                    temp.append(freq)

                time += 1
                cycle -= 1

            for freq in temp:
                heapq.heappush(heap, -freq)

            if heap:
                time += cycle

        return time