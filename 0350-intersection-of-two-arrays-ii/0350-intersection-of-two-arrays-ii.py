class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = {}
        intersection = []
        
        for num in nums1:
            if num in n1:
                n1[num] += 1
            else:
                n1[num] = 1
        
        for num in nums2:
            if num in n1 and n1[num] > 0:
                intersection.append(num)
                n1[num] -= 1
        
        return intersection