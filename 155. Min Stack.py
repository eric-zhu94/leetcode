#https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        self.stack = []
        self.length = 0
        self.low = float("inf")
        """
        initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.length +=1
        

    def pop(self) -> None:
        self.stack.pop()
        self.length -=1
        

    def top(self) -> int:
        return self.stack[self.length - 1]
        
        

    def getMin(self) -> int:
    #o(n) retrieval of minimum value, could keep track of minimum for o(1)
        mini = float("inf")
        for item in self.stack:
            if item < mini:
                mini = item
        return mini
                
                
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
