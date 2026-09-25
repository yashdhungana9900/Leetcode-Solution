class Solution(object):
    def pathSum(self, root, targetSum):
        result = []
        path = []

        def dfs(node, remaining):
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            # Leaf node
            if not node.left and not node.right:
                if remaining == 0:
                    result.append(path[:])
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)

            path.pop()

        dfs(root, targetSum)

        return result