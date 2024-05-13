class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        total_min = sum(nums[:3])
        length = len(nums)
        for i in range(length - 2):
            first = i + 1
            last = length - 1
            while first < last:
                total = nums[first] + nums[last] + nums[i]
                if abs(target - total) < abs(target - total_min):
                    total_min = total
                if target == total:
                    return total
                if target - total > 0:
                    first += 1
                else:
                    last -= 1
        return total_min