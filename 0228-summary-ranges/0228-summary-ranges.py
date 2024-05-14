class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        left = 0
        right = 0

        while right < len(nums):
            if right == len(nums) - 1 or nums[right + 1] != nums[right] + 1:
                if left == right:
                    answer.append(str(nums[left]))
                    left += 1
                    right +=1
                else:
                    answer.append(str(nums[left]) + "->" + str(nums[right]))
                    right += 1
                    left = right

            else:
                right += 1
                continue
        
        return answer