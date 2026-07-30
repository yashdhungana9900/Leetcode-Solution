#Leetcode-1929
#Easy #Array

class Solution:
    def getConcatenation(self, nums):
        ans = []

        for _ in range(2):
            for num in nums:
                ans.append(num)

        return ans