from sys import stdin, argv
fobj = stdin
if len(argv[1:]):
    fobj = open(argv[1])
#:= is an operator introduced in 3.8+ --> Walrus Operator

while (lineContent := fobj.readline()):
    print(lineContent.strip())
