class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currentMax = arr[-1]
        arr[-1] = -1
        
        for i in range(len(arr) - 2, -1, -1):
            temp = max(currentMax, arr[i])
            arr[i] = currentMax
            currentMax = temp
        
        return arr
        