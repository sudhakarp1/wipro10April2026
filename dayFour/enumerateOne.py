'''
    enumerate() --> giving numbers
'''
base=16
nums = ['0','1','2','3','4','5','6','7','8','9',
        'a','b','c','d','e','f' ]
vals =[]
for i, val in enumerate(nums[:base]):
    print(f'{i}-->{val}',end=' ')
    vals.append(i)

print(f'nums: {nums}')
print(f'vals: {vals}')

res = dict(zip(vals, nums))
print(f'res: {res}')

res = dict(zip(nums,vals))
print(f'res: {res}')
