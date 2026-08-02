class Solution(object):
    def searchRange(self, nums, target):

        def binarySearch(findFirst):

            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:

                mid = (left + right) // 2

                if nums[mid] == target:

                    ans = mid

                    if findFirst:
                        right = mid - 1
                    else:
                        left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return ans

        first = binarySearch(True)
        last = binarySearch(False)

        return [first, last]