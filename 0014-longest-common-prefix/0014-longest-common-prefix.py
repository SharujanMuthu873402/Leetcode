class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        count = 0

        if len(strs) == 1:
            return strs[0]

        while True:
            for i in range(len(strs) - 1):
                if len(strs[i]) - 1 < count or len(strs[i+1]) - 1 < count:
                    return answer
                
                if strs[i][count] != strs[i+1][count]:
                    return answer
                
            answer += strs[0][count]
            count += 1