from sys import stdin, argv
fobj = stdin
if len(argv[1:]):
    fobj = open(argv[1], 'r')

lineContent = fobj.readline()
while lineContent:
    print(lineContent.strip())
    lineContent = fobj.readline()
