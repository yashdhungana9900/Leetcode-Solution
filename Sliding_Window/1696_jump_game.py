from collections import deque

class Solution(object):
    def maxResult(self, nums, k):

        n = len(nums)

        dp = [0] * n
        dp[0] = nums[0]

        dq = deque([0])

        for i in range(1, n):

            # Remove indices outside the window
            while dq and dq[0] < i - k:
                dq.popleft()

            # Best previous score is at the front
            dp[i] = nums[i] + dp[dq[0]]

            # Maintain decreasing dp values
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            dq.append(i)

        return dp[n - 1]