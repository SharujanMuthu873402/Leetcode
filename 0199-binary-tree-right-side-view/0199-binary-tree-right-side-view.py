# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        
        def getValues(root, level):
            if root:
                if len(levels) == level:
                    levels.append([])
                levels[level].append(root.val)
            
                if root.right:
                    getValues(root.right, level+1)
                if root.left:
                    getValues(root.left, level+1)
        
        getValues(root,0)
        
        answer = []
        for array in levels:
            answer.append(array[0])
        
        return answer