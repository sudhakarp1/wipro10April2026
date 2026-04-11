w = 6
print('Su Mo Tu We Th Fr Sa')
print(f"{' ':3}" * w,end='')
for cnt in range(1, 31):
    print(f'{cnt:2}',end=' ')
    if (cnt + w ) % 7 == 0:
        print()