import heapq

lst = [99,77,88,22,23,11]
print(f'1 Before: {lst}')
heapq.heapify(lst)
print(f'2 After: {lst}')
#here eventhought data is stored in list but it behaves like a tree
heapq.heappush(lst, 5)
print(f'3 After: {lst}')
res = heapq.heappop(lst)
print(f'4 After: {lst} : res: {res}')