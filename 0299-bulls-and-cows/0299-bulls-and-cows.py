class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        seen = {}
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            if secret[i] in seen:
                seen[secret[i]] += 1
            else:
                seen[secret[i]] = 1
        
        for i in range(len(guess)):
            if guess[i] in seen and seen[guess[i]] != 0:
                cows += 1
                seen[guess[i]] -= 1
        
        cows = cows - bulls
        
        return str(bulls) + "A" + str(cows) + "B"