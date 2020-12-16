class MyStack:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.items.append(x)
        


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.items.pop()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.items[-1]
        


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.items == []
  



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
print(obj.push(1))
print(obj.push(2))
print(obj.push(3))
print(obj.push(4))

param_3 = obj.top()
print(param_3)
param_4 = obj.empty()
print(param_4)
param_2 = obj.pop()
print(param_2)
