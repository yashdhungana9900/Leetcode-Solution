import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        count = Counter(s)

        heap = []
        for char, freq in count.items():
            heapq.heappush(heap, (-freq, char))

        result = []

        while len(heap) >= 2:
            freq1, char1 = heapq.heappop(heap)
            freq2, char2 = heapq.heappop(heap)

            result.append(char1)
            result.append(char2)

            freq1 += 1
            freq2 += 1

            if freq1 < 0:
                heapq.heappush(heap, (freq1, char1))

            if freq2 < 0:
                heapq.heappush(heap, (freq2, char2))

        if heap:
            freq, char = heapq.heappop(heap)

            if -freq > 1:
                return ""

            result.append(char)

        return "".join(result)