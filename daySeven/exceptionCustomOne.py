class MyException(ValueError):
    def __init__(self, msg):
        mesg = f'Error Occurred: {msg}'
        super().__init__(mesg)

try:
    raise MyException('MyException Type')
except MyException as me:
    print(me)
except ValueError as ve:
    print(ve)
