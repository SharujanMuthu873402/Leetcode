# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        tree = TreeNode()
        mid = len(nums)//2
        tree.val = nums[mid]
        
        
        
        if mid != 0:
            tree.left = self.sortedArrayToBST(nums[:mid])
        if mid + 1 < len(nums):
            tree.right = self.sortedArrayToBST(nums[mid + 1:])
        
        
        return tree