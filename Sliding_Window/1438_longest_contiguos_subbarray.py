from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):

        max_dq = deque()
        min_dq = deque()

        left = 0
        answer = 0

        for right in range(len(nums)):

            # Maintain decreasing deque for maximum
            while max_dq and nums[max_dq[-1]] < nums[right]:
                max_dq.pop()

            max_dq.append(right)

            # Maintain increasing deque for minimum
            while min_dq and nums[min_dq[-1]] > nums[right]:
                min_dq.pop()

            min_dq.append(right)

            # Shrink window if invalid
            while nums[max_dq[0]] - nums[min_dq[0]] > limit:

                if max_dq[0] == left:
                    max_dq.popleft()

                if min_dq[0] == left:
                    min_dq.popleft()

                left += 1

            answer = max(answer, right - left + 1)

        return answer