import math

class Solution(object):
    def minEatingSpeed(self, piles, h):

        left = 1
        right = max(piles)

        while left < right:

            mid = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(pile / float(mid))

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left 