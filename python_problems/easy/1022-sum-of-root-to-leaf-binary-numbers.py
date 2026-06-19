# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return 0
        stack = [(root, 0)]
        while stack:
            node, curr = stack.pop()
            curr = curr*2 + node.val
            if not node.right and not node.left:
                ans += curr
            elif not node.right:
                stack.append((node.left, curr))
            elif not node.left:
                stack.append((node.right, curr))
            else:
                stack.append((node.left, curr))
                stack.append((node.right, curr))

        return ans

        
