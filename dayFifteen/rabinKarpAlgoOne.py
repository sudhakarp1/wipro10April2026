'''
    Rabin Karp Algorithm
'''

def rabinKarpAlgo(text, pattern):
    lenText, lenPattern = len(text), len(pattern)
    h = pow(256, lenPattern - 1) % 101

    p = t = 0
    #initial hash for the pattern and first text window
    for i in range(lenPattern):
        p = (256 * p + ord(pattern[i])) % 101 
        t = (256 * t + ord(text[i])) % 101
    
    for i in range(lenText - lenPattern + 1):
        if p == t:
            if text[i: i + lenPattern] == pattern:
                print(f'{pattern} found at {i} position')

        if i < lenText - lenPattern:
            #initial hash for consecutive text windows
            t = ( 256 * (t - ord(text[i]) * h) + ord(text[i+lenPattern])) % 101
            if t < 0:
                t+=101
    

if __name__ == '__main__':
    
    text = 'typing a lengthy string. this is lengthy. is this lengthy'
    pattern = 'length'
    rabinKarpAlgo(text, pattern)

    '''
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"    
    '''
