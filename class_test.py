class A(object):

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)


    def add(self, a, b):
        return a+b

class B(A):

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def sub(self, a, b):
        return  a-b


print(B().add(5,4))