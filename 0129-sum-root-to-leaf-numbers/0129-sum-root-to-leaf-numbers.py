# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def getSum(root, current):
            nonlocal total
            if root:
                current = current * 10 + root.val
                
                if not (root.left or root.right):
                    total += current
                
                getSum(root.left, current)
                getSum(root.right, current)
        
        getSum(root, 0)
        return total