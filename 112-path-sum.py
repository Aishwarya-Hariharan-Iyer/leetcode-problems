# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root == None:
            return False

        def hasSumSoFar(root, target, sumSoFar):
            sumSoFar = sumSoFar + root.val
            if root.right == None and root.left == None:
                return sumSoFar == target
            if root.left == None:
                return hasSumSoFar(root.right, target, sumSoFar)
            if root.right == None:
                return hasSumSoFar(root.left, target, sumSoFar)
            
            return hasSumSoFar(root.left, target, sumSoFar) or hasSumSoFar(root.right, target, sumSoFar)

        return hasSumSoFar(root, targetSum, 0)
        
