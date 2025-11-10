# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        if root == None:
            return True

        def find_height(root):
            if root. right == None and root.left == None:
                root.val = 0
                return root
            elif root.right == None:
                root.left = find_height(root.left)
                root.val = 1 + root.left.val
                return root
            elif root.left == None:
                root.right = find_height(root.right)
                root.val = 1 + root.right.val
                return root
            else:
                root.right = find_height(root.right)
                root.left = find_height(root.left)
                root.val = 1 + max(root.left.val, root.right.val)
                return root
        
        root = find_height(root)

        def confirm_balance(root):
            if root. right == None and root.left == None:
                return True
            elif root.left == None:
                return root.right.val < 1 and confirm_balance(root.right)
            elif root.right == None:
                return root.left.val < 1 and confirm_balance(root.left)
            else:
                return abs(root.left.val - root.right.val)  <= 1 and confirm_balance(root.left) and confirm_balance(root.right)

        return confirm_balance(root)
        
