class Solution(object):
    def dailyTemperatures(self, temperatures):

        answer = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:

                prev = stack.pop()
                answer[prev] = i - prev

            stack.append(i)

        return answer