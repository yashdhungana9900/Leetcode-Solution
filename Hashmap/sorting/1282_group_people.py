class Solution(object):
    def groupThePeople(self, groupSizes):
        groups = {}
        answer = []

        for i in range(len(groupSizes)):
            size = groupSizes[i]

            if size not in groups:
                groups[size] = []

            groups[size].append(i)

            if len(groups[size]) == size:
                answer.append(groups[size])
                groups[size] = []

        return answer