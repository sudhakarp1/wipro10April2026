def naiveSearch(text, pattern):
    lenText, lenPattern = len(text), len(pattern)

    for i in range(lenText - lenPattern + 1):
        found = True
        for j in range(lenPattern):
            if text[i + j] != pattern[j]:
                found = False
                break 
        
        if found:
            print(f'"{pattern}" found at {i} position')


if __name__ == '__main__':
    '''
    text = 'typing a lengthy string. this is lenghty. is this lengthy'
    pattern = 'this'

    naiveSearch(text, pattern)
    '''
    text = 'typing a lengthy string. this is lenghty. is this lengthy'
    pattern = 'length'

    naiveSearch(text, pattern)
