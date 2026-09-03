class Solution(object):
    def findMaxLength(self, nums):
        count = 0
        first_seen = {0: -1}
        answer = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if count in first_seen:
                answer = max(answer, i - first_seen[count])
            else:
                first_seen[count] = i

        return answer