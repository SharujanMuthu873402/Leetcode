class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = {}
        answer = []
        
        for num in nums1:
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
        
        for num in nums2:
            if num in nums and nums[num] > 0:
                answer.append(num)
                nums[num] = 0
        
        return answer