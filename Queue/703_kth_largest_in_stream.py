import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.heap = []

        for num in nums:
            heapq.heappush(self.heap, num)

            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]