# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def mini_symm_check(r1, r2):
            if r1 == None and r2 == None:
                return True
            if r1 == None or r2 == None:
                return False
            if r1.val != r2.val:
                return False
            return mini_symm_check(r1.left, r2.right) and mini_symm_check(r1.right, r2.left)

        return mini_symm_check(root.left, root.right)
        
