'''
    first create LPS table
        use the lps table for skipping number of characters in your kmpAlgo
'''

def createLPSTable(pattern):
    lpsTbl = [0] * len(pattern)
    i, j = 1, 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j+=1
            lpsTbl[i] = j 
            i+=1
        else:
            if j != 0:
                j = lpsTbl[j - 1]
            else:
                lpsTbl[i] = 0 
                i += 1
    return lpsTbl

def kmpAlgo(text, pattern):
    lpsTbl = createLPSTable(pattern)
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i, j = i + 1, j + 1
        
        if j == len(pattern):
            print(f'{pattern} found at {i-j} position')
            j = lpsTbl[j-1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lpsTbl[j - 1]
            else:
                i += 1

if __name__ == '__main__':
    '''
    text = 'typing a lengthy string. this is lengthy. is this lengthy'
    pattern = 'length'
    '''

    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"    
    
    
    print(f'{pattern} : {createLPSTable(pattern)}')
    kmpAlgo(text, pattern)