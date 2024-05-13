class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def generateParenthesisHelper(open, close, brackets):
            if close > open:
                temp = brackets + ')'
                generateParenthesisHelper(open, close - 1, temp)
            
            if open > 0:
                temp = brackets + '('
                generateParenthesisHelper(open-1, close, temp)
            
            if open == 0 and close == 0:
                answer.append(brackets)
            
            return
        
        generateParenthesisHelper(n, n, "")
        return answer