'''
    Tower if Hanoi --> recursion
    towerHanoi(3, SRC, AUX, DEST)
    | towerHanoi(2, SRC, DEST, AUX)
    |    |-- towerHanoi(1, SRC, AUX, DEST) --> Move SRC-->DEST
    |    |-- Move disk 2 SRC-->AUX
    |    |-- towerHanoi(1, DEST, SRC, AUX) --> Move DEST-->AUX
    |
    |-- Move disk 3 SRC-->DEST
    |
    |-- towerHanoi(2, AUX, SRC, DEST)
        |-- towerHanoi(1, AUX, DEST, SRC) --> Move AUX-->SRC
        |-- Move disk 2 AUX-->DEST
        |-- towerHanoi(1, SRC, AUX, DEST) --> Move SRC-->DEST
'''
def towerHanoi(num, src, aux, dest):
    if num == 1:
        print(f'Move disk 1: from {src} --> {dest}')
        return
    towerHanoi(num - 1, src, dest, aux)
    print(f'Move disk {num}: from {src} --> {dest}')
    towerHanoi(num - 1,aux, src, dest)

if __name__ == '__main__':
    towerHanoi(3, 'SRC', 'AUX', 'DEST')