class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        answer = []
        if len(nums) == 2:
            return nums
        
        for i in range(len(nums) - 1):
            if nums[i] not in nums[0:i] + nums[i + 1:len(nums)]:
                answer.append(nums[i])
        
        if len(answer) == 1:
            answer.append(nums[-1])
        
        return answer