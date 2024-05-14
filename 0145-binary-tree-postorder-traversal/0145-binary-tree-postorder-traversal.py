# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            nodes = []
            
            if root.left:
                nodes = self.postorderTraversal(root.left)
            if root.right:
                nodes += self.postorderTraversal(root.right)
            nodes += [root.val]
            
            return nodes
        
        return []