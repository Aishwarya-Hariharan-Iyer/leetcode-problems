class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n
        

    def allocate(self, size: int, mID: int) -> int:

        lpr = 0
        rpr = 0
        l = len(self.memory)
        count = 0

        while rpr < l:
            if self.memory[rpr] == 0:
                count += 1
                rpr += 1
                if count == size:
                    break
            else:
                lpr = rpr+1
                rpr += 1
                count = 0
        
        if count != size:
            return -1

        self.memory[lpr: rpr] = [mID] * size
        return lpr

        

    def freeMemory(self, mID: int) -> int:
        units = 0
        for i in range(len(self.memory)):
            if self.memory[i]== mID:
                self.memory[i] = 0
                units += 1
        return units
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)