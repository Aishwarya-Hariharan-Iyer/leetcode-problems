class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.values = dict()
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey] = value
        vals_output = []
        while self.ptr <= self.n:
            if self.values.get(self.ptr, None) is not None:
                vals_output.append(self.values[self.ptr])
                self.ptr += 1
            else:
                break
        return vals_output
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.values = ["X"] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey-1] = value
        vals_output = []
        while self.ptr < self.n and self.values[self.ptr] != "X":
            vals_output.append(self.values[self.ptr])
            self.ptr += 1
        return vals_output
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)