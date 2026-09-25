# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # No left child
            if not root.left:
                return root.right

            # No right child
            if not root.right:
                return root.left

            # Two children
            current = root.right

            while current.left:
                current = current.left

            root.val = current.val

            root.right = self.deleteNode(root.right, current.val)

        return root