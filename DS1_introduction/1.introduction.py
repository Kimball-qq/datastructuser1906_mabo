"""
如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
"""
# import time
# start_time = time.time()

# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range (0,1001):
#             if a**2+b**2== c**2 and a+b+c==1000:
#                 print(a,b,c)

# end_time = time.time()
# print("耗时%s"%(end_time-start_time))



# import time
# start_time = time.time()

# for a in range(0,1001):
#     for b in range(0,1001):
#         c = 1000-a-b
#         if a**2 + b**2 == c**2:
#             print("a=%d,b=%d,c=%d"%(a,b,c))
            
# end_time = time.time()
# print("耗时%s"%(end_time-start_time))


#计算1-5000的和  普通算法，高斯算法

import time
start_time = time.time()

num = 0
for a in range(0,5001):

    num = num + a


end_time = time.time()



# 练习求列表中的最小值






