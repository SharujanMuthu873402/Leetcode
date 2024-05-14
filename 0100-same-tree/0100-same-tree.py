# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if self.getValues(p) == self.getValues(q):
            return True
        return False
    
    
    def getValues(self, tree):
        if tree:
            return [tree.val] + self.getValues(tree.left) + self.getValues(tree.right)
        return [None]