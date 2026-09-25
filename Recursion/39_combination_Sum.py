class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])

                # i, not i + 1 → can reuse the same number
                backtrack(i, path, total + candidates[i])

                path.pop()

        backtrack(0, [], 0)

        return result