# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root == None:
            return root
        elif root.left == None and root.right == None:
            return root
        elif root.left and root.right:
            new_left = self.invertTree(root.right)
            new_right = self.invertTree(root.left)
            root.left = new_left
            root.right = new_right
            return root
        elif root.left:
            root.right = self.invertTree(root.left)
            root.left = None
            return root
        else:
            root.left = self.invertTree(root.right)
            root.right = None
            return root
