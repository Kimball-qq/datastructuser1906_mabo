'''
列表：
生成列表：+ append  列表推导式  list()
删除;

字典
生成字典：
删除：
'''
def test1():
    l = []
    for i in range(1000):
      l = l + [i]

def test2():
   l = []
   for i in range(1000):
      l.append(i)

def test3():
   l = [i for i in range(1000)]

def test4():
   l = list(range(1000))

from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("+ ",t1.timeit(number=1000), "seconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "seconds")
t3 = Timer("test3()", "from __main__ import test3")
print("列表推导式 ",t3.timeit(number=1000), "seconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list ",t4.timeit(number=1000), "seconds")




















