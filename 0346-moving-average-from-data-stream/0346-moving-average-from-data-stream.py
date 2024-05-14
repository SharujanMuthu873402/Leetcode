class MovingAverage:

    def __init__(self, size: int):
        self.count = 0
        self.sum = 0
        self.max = size
        self.stack = []
        

    def next(self, val: int) -> float:
        self.sum += val
        self.count += 1
        self.stack.insert(0, val)
        
        if self.count > self.max:
            self.sum -= self.stack.pop()
            self.count -= 1
        
        return self.sum/self.count
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)