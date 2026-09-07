class Solution(object):
    def maxDistance(self, position, m):
        position.sort()

        left = 1
        right = position[-1] - position[0]
        answer = 0

        while left <= right:
            mid = left + (right - left) // 2

            balls = 1
            last = position[0]

            for i in range(1, len(position)):
                if position[i] - last >= mid:
                    balls += 1
                    last = position[i]

            if balls >= m:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer