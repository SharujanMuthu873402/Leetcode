class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) > 1:
            return False
        
        if nums[0] == 0 and len(nums) == 1:
            return True

        def check(pointer):
            count = 0

            for i in range(pointer-1, -1, -1):
                count += 1
                if nums[i] > count:
                    return True
            
            return False

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                skip = check(i)
                if skip == False:
                    return False

        return True