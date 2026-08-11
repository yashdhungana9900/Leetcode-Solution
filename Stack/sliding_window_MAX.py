from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):

        dq = deque()
        answer = []

        for i in range(len(nums)):

            # 1. Remove elements outside the window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Remove smaller elements
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Window has reached size k
            if i >= k - 1:
                answer.append(nums[dq[0]])

        return answer