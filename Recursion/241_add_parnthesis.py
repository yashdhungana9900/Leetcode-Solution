class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        result = []

        for i, ch in enumerate(expression):
            if ch in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for a in left:
                    for b in right:
                        if ch == "+":
                            result.append(a + b)
                        elif ch == "-":
                            result.append(a - b)
                        else:
                            result.append(a * b)

        if not result:
            result.append(int(expression))

        return result
        