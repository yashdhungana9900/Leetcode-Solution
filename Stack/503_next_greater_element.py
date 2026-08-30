class Solution(object):
    def nextGreaterElements(self, nums):

        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * n):

            index = i % n

            while stack and nums[stack[-1]] < nums[index]:
                result[stack.pop()] = nums[index]

            if i < n:
                stack.append(index)

        return result