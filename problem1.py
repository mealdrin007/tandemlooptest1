# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#     Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#     Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class Addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        r=self.a+self.b
        print(r)


class Subtration:
     def __init__(self,a,b):
        self.a=a
        self.b=b
        r=self.a-self.b
        print(r)


class Multiplication:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        r=self.a*self.b
        print(r)


class Division:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        r=self.a/self.b
        print(r)


while True:
    print("You can enter type of operations +,-,*,/ or addition,subtration,multiplication,division")
    a,b,c=float(input("a=")),float(input("b=")),input("type of operation=")
    if c=="+" or c=="addition":
        x=Addition(a,b)
    elif c=="-" or c=="subtration":
        x=Subtration(a,b)
    elif c=="*" or c=="multiplication":
        x=Multiplication(a,b)
    elif c=="/" or c=="division":
        x=Division(a,b)
    else:
        print("invalid operation")