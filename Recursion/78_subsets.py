class Solution(object):
    def subsets(self, nums):
        result = []

        def backtrack(index, path):
            if index == len(nums):
                result.append(path[:])
                return

            # Choose
            path.append(nums[index])
            backtrack(index + 1, path)

            # Skip
            path.pop()
            backtrack(index + 1, path)

        backtrack(0, [])

        return result