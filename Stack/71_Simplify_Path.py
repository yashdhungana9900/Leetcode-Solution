class Solution(object):
    def simplifyPath(self, path):

        stack = []

        parts = path.split("/")

        for part in parts:

            if part == "" or part == ".":
                continue

            elif part == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(part)

        return "/" + "/".join(stack)