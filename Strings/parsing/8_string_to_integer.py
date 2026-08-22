class Solution(object):
    def myAtoi(self, s):

        i = 0
        n = len(s)

        # 1. Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == "-":
            sign = -1
            i += 1
        elif i < n and s[i] == "+":
            i += 1

        # 3. Build number
        num = 0

        while i < n and s[i].isdigit():

            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        # 4. Handle 32-bit integer limits
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN

        if num > INT_MAX:
            return INT_MAX

        return num