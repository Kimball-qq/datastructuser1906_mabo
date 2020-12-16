'''
队列: 队列是一系列元素的集合，新元素的加入的一端称作“队尾（rear）”
    已有元素移出的一端称作“队首（front）”
    ---------------------------------
    rear                         front
    ---------------------------------
    特点：先进先出
    抽象数据类型（ADT）
        Queue():创建一个空队列对象，无参数，返回空的队列
        enqueue(item):将数据添加到队尾，有参数，无返回值
        dequeue():将数据从队首移出，无参数，返回值为队首数据项
        isEmpty():判断队列是否为空，无参数，返回布尔值
        size():返回队列中元素的个数，无需参数

用python list实现队列
    队尾在列表的0的位置
    enqueue     insert()   O(n)
    dequeue     pop()      O(1)
'''
# class  Queue():
#     def __init__(self):
#         self.items = []
    
#     def enqueue(self,item):
#         self.items.insert(0,item)
    
#     def dequeue(self):
#         return self.items.pop()
    
#     def isEmpty(self):
#         return self.items == []

#     def size(self):
#         return len(self.items)

# a = Queue()
# b = [1,2,3,4,5,6]
# for c in  b:
#     a.enqueue(c)
#     print(a.size())
#     print(a.isEmpty())
#     # print(a.dequeue())
#     print('----')
# print(a.items)


# 马铃薯游戏（击鼓传花）选定一个人作为开始人，数到num个人，将此人淘汰
from pythonds.basic.queue import Queue

name_list = ['0','1','2','3','4','5','6','7','8','9']
num = 7

def send_flower(name_list,num):
    q = Queue()
    for name in name_list:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        print(q.dequeue())
    return q.dequeue()

send_flower(name_list,num)



























