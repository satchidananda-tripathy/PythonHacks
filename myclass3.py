#Class method and Class variable

class myClass3:
    col='Red'
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def prnt_dtls(self):
        print(f"Length and Breadth of the rectangle is {self.x} and {self.y}")
    @classmethod
    def print_color(cls):
        print("Color of the Rectangle is :",end=' ')
        print(myClass3.col)


obj = myClass3(2,3)
obj.prnt_dtls()
obj.print_color()
obj1 = myClass3(5,3)
obj1.prnt_dtls()
obj1.print_color()

