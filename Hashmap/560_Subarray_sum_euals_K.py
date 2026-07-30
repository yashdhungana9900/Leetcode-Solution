# LeetCode 560 - Subarray Sum Equals K
# Topic: Hashmap + Prefix Sum
# Difficulty: Medium

class Solution:
    def subarraySum(self, nums, k):
        prefix_count = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_count:
                count += prefix_count[prefix_sum - k]

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count