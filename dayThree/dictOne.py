dtOne= {'one':1, 'two':2, 'three':3,'four': 44}

print(f'get: {dtOne.get("four", 4)}')
print(f'keys: {dtOne.keys()}')
print(f'Values: {dtOne.values()}')
print(f'Values: {dtOne.items()}')

for k,v in dtOne.items():
    print(f'{k}--> {v}', end='  ')
