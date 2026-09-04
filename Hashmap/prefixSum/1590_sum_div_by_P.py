class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums)
        rem = total % p

        if rem == 0:
            return 0

        prefix = 0
        last_seen = {0: -1}
        answer = len(nums)

        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % p

            needed = (prefix - rem) % p

            if needed in last_seen:
                answer = min(answer, i - last_seen[needed])

            last_seen[prefix] = i

        if answer == len(nums):
            return -1

        return answer
        