'''
    Intro to sys module
'''

import sys 

print(sys.argv)
print(sys.path)

print(sys.version)
print(sys.platform)
print(sys.getrecursionlimit())
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())

print(sys.modules.keys())