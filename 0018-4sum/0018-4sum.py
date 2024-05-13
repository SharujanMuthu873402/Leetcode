class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                for w in range(j + 1, len(nums) - 1):
                    add = nums[i] + nums[j] + nums[w]
                    need = target - add
                    if need in nums[w + 1::] and [nums[i], nums[j], nums[w], need] not in answer:
                        answer.append([nums[i], nums[j], nums[w], need])
        return answer