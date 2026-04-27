class MyString:
    def __init__(self, data):
        self.string = list(data)
    
    def __str__(self):
        return f'{"".join(self.string)}'
    
    def __add__(self, other):
        temp = None
        if isinstance(other, MyString):
            temp  = MyString(self.string + other.string)
        elif isinstance(other, str):
            temp = MyString(self.string + list(other))
        else:
            temp = MyString(self.string + list(str(other)))
        return temp
    
    def reverse(self):
        return self.string[::-1]
    
    def slice(self, start, end):
        return ''.join(self.string[start:end])


if __name__ == '__main__':
    someString = MyString('Hello World')
    print(someString)

    newStr = someString + 'How are you'
    print(newStr)

    print(newStr.slice(0, 5))


