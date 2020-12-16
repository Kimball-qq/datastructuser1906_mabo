'''
栈（堆叠栈）
特点：先进后出
栈顶： 增加和删除的操作都是在栈顶完成
栈底
抽像数据类型（ADT）
Stack():创建空栈
push(item):添加元素，有参数，无返回值
pop():删除元素，无参数，返回被删除的元素，堆栈被修改
peek()：返回栈顶元素，堆栈不被修改
size（）：无参数，返回元素个数，整数
isEmpty():无参数，返回布尔值


'''


class Strck():
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []

a = Strck()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
print(a.items)
print(a.peek())

print(a.pop())
print(a.size())
print(a.peek())










































