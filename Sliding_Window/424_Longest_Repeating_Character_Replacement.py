class Solution(object):
    def characterReplacement(self, s, k):

        count = {}
        left = 0
        max_freq = 0
        answer = 0

        for right in range(len(s)):

            count[s[right]] = count.get(s[right], 0) + 1

            max_freq = max(max_freq, count[s[right]])

            window_size = right - left + 1

            if window_size - max_freq > k:
                count[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer