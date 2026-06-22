'''
Thought Process:
Hompage
hist = [A, B, C, D,.....
Visit B -> hist[:curr] + B
Back -> hisr[min(curr-steps, 0)]
Forward -> hist[max(curr+steps, len(steps))]

'''
class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.current_pos = 0
        

    def visit(self, url: str) -> None:
        self.hist = self.hist[:self.current_pos+1] + [url]
        self.current_pos = len(self.hist) - 1 #no 'forward' history any more


    def back(self, steps: int) -> str:
        if self.current_pos - steps <= 0:
            self.current_pos = 0
        else:
            self.current_pos = self.current_pos - steps
        return self.hist[self.current_pos]
        

    def forward(self, steps: int) -> str:
        if self.current_pos + steps >= len(self.hist):
            self.current_pos = len(self.hist) - 1
        else:
            self.current_pos = self.current_pos + steps
        return self.hist[self.current_pos]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)