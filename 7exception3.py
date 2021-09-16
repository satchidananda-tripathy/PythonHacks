## Exceptions during runtime can break the program which needs to be handled.
# try (block causing exception) except (the catch block)  finally (always executed block)  raise (user defined exception)
class myException(Exception):
    def __init__(self,x):
        self.x = x


    def throw_excp(self):
        if self.x == 0:
            raise Exception("You can not initialize class with  0")

obj = myException(2)
try:
    obj.throw_excp()
except Exception as e:
    print(e)
else:
    print('There is no exception, this object looks good')
finally:
    print('Above depicts how the exception work!!')