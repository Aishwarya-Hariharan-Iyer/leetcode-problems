# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def set_diameters(root, max_val):
            if root.left == None and root.right == None:
                root.val == 0
                return root
            if root.left == None:
                root.right = set_diameters(root.right)
                root.val = 1 + root.right.val
                return root
            if root.right == None:
                root.left = set_diameters(root.left)
                root.val = 1 + root.left.val
                return root
            root.left = set_diameters(root.left)
            root.right = set_diameters(root.right)
            root.val = 2 + root.left.val + root.right.val
            return root
        
        root = set_diameters(root)
        print(root)
        return root.val

        