#leetcode 347 
#medium

class Solution(object):
    def topKFrequent(self, nums, k):
         count = {}

        # Count frequency
         for num in nums:
            count[num] = count.get(num, 0) + 1

        # Sort by frequency (highest first)
         sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

         result = []

        # Take first k elements
         for i in range(k):
            result.append(sorted_items[i][0])

         return result

   