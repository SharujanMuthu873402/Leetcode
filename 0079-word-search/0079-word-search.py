class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                seen = []
                if board[i][j] == word[0]:
                    #print(board[i][j])
                    seen.append([i,j])
                    if word[1::] == "":
                        return True
                    found = self.search(board, i, j, word[1:], seen)
                    if found:
                        return True
        return False
                    
    
    
    def search(self, board, i, j, word, seen):
        if j < len(board[i]) - 1:
            if([i, j+1] not in seen and board[i][j+1] == word[0]):
                #print(word + ": " + board[i][j+1])
                if word[1:] == "":
                    return True
                seen.append([i, j+1])
                if self.search(board, i, j+1, word[1:], seen):
                    return True
                seen.pop()
        if j > 0:
            if([i, j-1] not in seen and board[i][j-1] == word[0]):
                #print(word + ": " + board[i][j-1])
                if word[1:] == "":
                    return True
                seen.append([i, j-1])
                if self.search(board, i, j-1, word[1:], seen):
                    return True
                seen.pop()
        if i < len(board) - 1:
            if([i+1, j] not in seen and board[i+1][j] == word[0]):
                #print(word + ": " + board[i+1][j])
                if word[1:] == "":
                    return True
                seen.append([i+1, j])
                if self.search(board, i+1, j, word[1:], seen):
                    return True
                seen.pop()
        if i > 0:
            if([i-1, j] not in seen and board[i-1][j] == word[0]):
                #print(word + ": " + board[i-1][j])
                if word[1:] == "":
                    return True
                seen.append([i-1, j])
                if self.search(board, i-1, j, word[1:], seen):
                    return True
                seen.pop()
        return False