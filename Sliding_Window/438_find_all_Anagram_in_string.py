class Solution(object):
    def findAnagrams(self, s, p):

        if len(p) > len(s):
            return []

        count_p = {}
        count_window = {}

        for char in p:
            count_p[char] = count_p.get(char, 0) + 1

        result = []
        left = 0

        for right in range(len(s)):

            count_window[s[right]] = count_window.get(s[right], 0) + 1

            # Keep window size equal to len(p)
            if right - left + 1 > len(p):
                count_window[s[left]] -= 1

                if count_window[s[left]] == 0:
                    del count_window[s[left]]

                left += 1

            # Check if window is an anagram
            if count_window == count_p:
                result.append(left)

        return result