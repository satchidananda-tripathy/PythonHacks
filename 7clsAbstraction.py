# A method or variable preceeded by two underscore is  private which can not be accessed by others.
#To call a private member we have to use _<classname>__membername Normally we don't call private method but if we have to then we do


class Test:
    def pub(self):
        print("I am a public funciton")
    def __priv(self):
        print("I am a private function")

t = Test()
t.pub()

print('With t. the private function can not be accessed')
print('So we have to use _Test__priv()')
t._Test__priv()
