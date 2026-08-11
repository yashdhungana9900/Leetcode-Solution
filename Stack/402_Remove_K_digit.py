class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []

        for digit in num:

            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # If removals are still left, remove from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')

        if result == "":
            return "0"

        return result
        