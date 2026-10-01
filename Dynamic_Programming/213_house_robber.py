class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        def rob_line(arr):
            prev2 = 0
            prev1 = 0

            for money in arr:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current

            return prev1

        return max(
            rob_line(nums[:-1]),
            rob_line(nums[1:])
        )