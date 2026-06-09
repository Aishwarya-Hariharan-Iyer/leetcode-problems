class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.vals = [0]*size
        self.ptr = 0
        self.running_sum = 0
        self.hasAttainedSize = False
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.ptr < self.size:
            self.running_sum += val - self.vals[self.ptr]
            self.vals[self.ptr] = val
            self.ptr += 1
            return float(self.running_sum)/(self.ptr) if not self.hasAttainedSize else float(self.running_sum)/(self.size)
        else:
            self.hasAttainedSize = True
            self.ptr = 0
            self.running_sum += val - self.vals[self.ptr]
            self.vals[self.ptr] = val
            self.ptr += 1
            return float(self.running_sum)/self.size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
