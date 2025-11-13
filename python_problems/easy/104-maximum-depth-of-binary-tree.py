# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if root == None:
            return 0
        elif root.right == None and root.left == None:
            return 1
        elif root.right == None:
            return 1 + self.maxDepth(root.left)
        elif root.left == None:
            return 1 + self.maxDepth(root.right)
        else:
            return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
        
