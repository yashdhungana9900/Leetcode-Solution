class Solution(object):
    def maximumSubarraySum(self, nums, k):
        count = {}
        current_sum = 0
        answer = 0
        left = 0

        for right in range(len(nums)):
            current_sum += nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1

            # Keep window size <= k
            if right - left + 1 > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                current_sum -= nums[left]
                left += 1

            # Exactly k elements and all distinct
            if right - left + 1 == k and len(count) == k:
                answer = max(answer, current_sum)

        return answer