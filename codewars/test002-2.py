# L = ['Bart', 'Lisa', 'Adam']
# for i in L:
#     print("hello," + i)
#
# n = 1
# while n <= 100:
#     if n > 10: # 当n = 11时，条件满足，执行break语句
#         break # break语句会结束当前循环
#     print(n)
#     n = n + 1
# print('END')

# print([x * x for x in range(1, 11)])
# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# print([k + '=' + v for k, v in d.items()])
#
# y = 1

# L = ['Hello', 'World', 18, 'Apple', None]
# print([s.lower() for s in L])


#
# print([x * x if x == 0 else -x for x in range(1, 11)])

L1 = ['Hello', 'World', 18, 'Apple', None]

print([i.lower() for i in L1 if isinstance(i, str)])
