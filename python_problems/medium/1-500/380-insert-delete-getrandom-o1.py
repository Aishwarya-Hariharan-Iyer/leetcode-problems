import random

class RandomizedSet:

    def __init__(self):
        self.set = set()
        self.list = []
        self.dict = dict()
        self.count = 0
        

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set.add(val)
        self.list.append(val)
        self.dict[val] = self.count
        self.count += 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        self.set.remove(val)
        curr_ind = self.dict[val]
        if self.count > 1: #atleast one other element present
            self.list[curr_ind] = self.list[-1]
            self.dict[self.list[-1]] = curr_ind
            self.list.pop()
        else:
            self.list = [] 
        self.count -= 1
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        r = random.randint(0, self.count-1)
        return self.list[r]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()