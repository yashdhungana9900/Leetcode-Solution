class Solution(object):
    def smallestDivisor(self, nums, threshold):
        left = 1
        right = max(nums)

        while left <= right:
            mid = left + (right - left) // 2

            total = 0

            for num in nums:
                total += (num + mid - 1) // mid

            if total <= threshold:
                right = mid - 1
            else:
                left = mid + 1

        return left