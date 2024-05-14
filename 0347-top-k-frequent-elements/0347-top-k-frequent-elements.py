class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        freq = {}

        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            
            else:
                answer.append(nums[i])
                freq[nums[i]] = 1

        k = len(answer) - k

        def quickSelect(left, right):
            pivot = freq[answer[right]]
            p = left

            for i in range(left, right):
                if freq[answer[i]] <= pivot:
                    answer[i], answer[p] = answer[p], answer[i]
                    p += 1
            
            answer[right], answer[p] = answer[p], answer[right]

            if p == k:
                return answer[p:]
            
            elif p > k:
                return quickSelect(left, p-1)
            
            else:
                return quickSelect(p+1, right)

        return quickSelect(0, len(answer) - 1)