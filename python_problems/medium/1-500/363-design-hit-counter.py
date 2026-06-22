from collections import deque

class HitCounter:

    def __init__(self):
        self.q = deque()
        

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.q and self.q[0] <= timestamp-300:
            self.q.popleft()
        return len(self.q)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

class HitCounter:

    def __init__(self):
        self.hitCount = dict() #timestamp -> hit count
        

    def hit(self, timestamp: int) -> None:
        self.hitCount[timestamp] = self.hitCount.get(timestamp, 0) + 1


    def getHits(self, timestamp: int) -> int:
        s = 0
        for j in range(timestamp, timestamp-300, -1):
            s += self.hitCount.get(j, 0)
        return s


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

