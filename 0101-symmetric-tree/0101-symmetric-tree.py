# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left and root.right:
            return self.isSame(root.left, root.right)
        if root.left and not root.right or not root.left and root.right:
            return False
        return True
    
    def isSame(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 and t2 or t1 and not t2:
            return False
        if t1.val != t2.val:
            return False
        return self.isSame(t1.left, t2.right) and self.isSame(t1.right, t2.left)