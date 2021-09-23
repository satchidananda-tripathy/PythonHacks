## Exceptions during runtime can break the program which needs to be handled.
# try (block causing exception) except (the catch block)  finally (always executed block)  raise (user defined exception)
try:
    x=5/0
    print(x)
except:
    print('You can not divide a number by zero')

try:
    x=51/0
    print(x)
except Exception as e:
    print(e)