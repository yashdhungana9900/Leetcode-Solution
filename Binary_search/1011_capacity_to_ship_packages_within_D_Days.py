class Solution(object):
    def shipWithinDays(self, weights, days):
         left = max(weights)
         right = sum(weights)

         while left < right:

            mid = (left + right) // 2

            days_needed = 1
            current_weight = 0

            for weight in weights:

                if current_weight + weight > mid:
                    days_needed += 1
                    current_weight = 0

                current_weight += weight

            if days_needed <= days:
                right = mid
            else:
                left = mid + 1

         return left
      
        