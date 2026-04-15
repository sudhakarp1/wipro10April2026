'''
    Usage of os Package.
    from pathlib import Path('.') #normally i use
'''

import os 

path = '.'
print(os.path.abspath(path))
print(path)

newPath = os.path.join(path, 'myPkgTwo')
print(newPath)
print(os.path.abspath(newPath))
print(os.path.exists(newPath))
print(os.path.isfile(newPath))
print(os.path.isdir(newPath))

print(os.environ['PYTHONPATH'])