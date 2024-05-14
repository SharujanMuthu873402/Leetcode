class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index = {}
        
        for i in range(len(nums)):
            if nums[i] not in index:
                index[nums[i]] = i
            else:
                if abs(i - index[nums[i]]) <= k:
                    return True
                else:
                    index[nums[i]] = i
        
        return False