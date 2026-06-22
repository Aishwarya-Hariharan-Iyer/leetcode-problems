from collections import deque

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = dict() #id -> origin time
        self.unexpiredTokens = deque()
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime
        self.unexpiredTokens.append(tokenId)
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.tokens.get(tokenId, -1) != -1 and self.tokens[tokenId] + self.timeToLive > currentTime:
            self.tokens[tokenId] = currentTime
            self.unexpiredTokens.remove(tokenId)
            self.unexpiredTokens.append(tokenId)
            

        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.unexpiredTokens and self.tokens[self.unexpiredTokens[0]] + self.timeToLive <= currentTime:
            self.unexpiredTokens.popleft()
        return len(self.unexpiredTokens)
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = dict() #id -> origin time
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.tokens.get(tokenId, -1) != -1 and self.tokens[tokenId] + self.timeToLive > currentTime:
            self.tokens[tokenId] = currentTime
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for i in self.tokens.keys():
            ori = self.tokens[i]
            if self.timeToLive + ori > currentTime:
                count += 1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)