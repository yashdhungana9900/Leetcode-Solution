class Solution(object):
    def reverseWords(self, s):

        words = s.split()

        for i in range(len(words)):
            words[i] = words[i][::-1]

        return " ".join(words)