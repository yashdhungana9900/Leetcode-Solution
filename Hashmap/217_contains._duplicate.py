# LeetCode 217 - Contains Duplicate
# Topic: Hashmap
# Difficulty: Easy

class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
    