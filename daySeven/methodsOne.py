class Sample:
    @classmethod
    def methodOne(cls):
        print('class Method')

    @staticmethod
    def methodTwo():
        print('Static method here')

if __name__ == '__main__':
    objOne = Sample()
    objOne.methodOne()
    objOne.methodTwo()