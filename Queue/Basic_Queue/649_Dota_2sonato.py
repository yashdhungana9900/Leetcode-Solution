
from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)

        radiant = deque()
        dire = deque()

        # Store indices
        for i in range(n):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:

            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                # Radiant bans Dire
                radiant.append(r + n)
            else:
                # Dire bans Radiant
                dire.append(d + n)

        if radiant:
            return "Radiant"
        else:
            return "Dire"
        