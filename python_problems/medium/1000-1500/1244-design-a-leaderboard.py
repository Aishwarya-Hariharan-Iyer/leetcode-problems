class Leaderboard:

    def __init__(self):
        self.leaderboard = dict()
        

    def addScore(self, playerId: int, score: int) -> None:
        self.leaderboard[playerId] = self.leaderboard.get(playerId, 0) + score
        

    def top(self, K: int) -> int:
        vals = list(self.leaderboard.values())
        vals.sort(reverse=True)
        return sum(vals[:K])
        

    def reset(self, playerId: int) -> None:
        self.leaderboard[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)