class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True

        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

    def sameTree(self, a, b):
        if not a and not b:
            return True

        if not a or not b:
            return False

        if a.val != b.val:
            return False

        return (
            self.sameTree(a.left, b.left) and
            self.sameTree(a.right, b.right)
        )