class MinStack:

    def __init__(self):
        self.item = []
        

    def push(self, val: int) -> None:
        self.item.append(val)
        

    def pop(self) -> None:
        return self.item.pop()
        

    def top(self) -> int:
        return self.item[-1]

        

    def getMin(self) -> int:
        return min(self.item)   


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
