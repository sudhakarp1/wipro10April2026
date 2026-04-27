'''

'''

def badCharHeuristic(pattern):
    badCharList = [-1] * 256
    for i in range(len(pattern)):
        badCharList[ord(pattern[i])] = i 
    return badCharList

def boyerMoore(text, pattern):
    badCharList = badCharHeuristic(pattern)
    lenText, lenPattern = len(text), len(pattern)
    i = 0
    while i <= lenText - lenPattern:
        j = lenPattern - 1

        while j>=0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            print(f'{pattern} found at {i} position')
            i += (lenPattern - badCharList[ord(text[i + lenPattern])] if i + lenPattern < lenText else 1)
        else:
            i+= max(1, j - badCharList[ord(text[i + lenPattern])])

if __name__ == '__main__':
    
    text = 'typing a lengthy string. this is lengthy. is this lengthy'
    pattern = 'length'
    boyerMoore(text, pattern)