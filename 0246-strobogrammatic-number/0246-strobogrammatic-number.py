class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        nums = {"0": "0", "1" : "1", "6":"9", "8":"8", "9":"6"}
        
        num = list(num)
        answer = []
        
        for i in range(len(num) - 1, -1, -1):
            if num[i] in nums:
                answer.append(nums[num[i]])
            else:
                return False
        

        return answer == num