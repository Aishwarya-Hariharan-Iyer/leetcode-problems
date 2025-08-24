# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        elif p.right == None and q.right == None and p.left == None and q.left == None:
            return p.val == q.val
        elif p.right == None and q.right == None:
            return self.isSameTree(p.left, q.left)
        elif p.left == None and q.left == None:
            return self.isSameTree(p.right, q.right)
        elif p.right == None or q.right == None or p.left == None or q.left == None:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
