#Leetcode- 1920
#Arrays

class Solution:
    def buildArray(self, nums):
        ans = []

        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans