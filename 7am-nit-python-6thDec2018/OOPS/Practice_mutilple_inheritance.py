class A():
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")
        self.__param = 'param'
        self.cheg = "cheg"
    def agni(self):
        print("agni")

class C(B):
    def __init__(self):
        super().__init__()
        print("C")

c = C()
print(c.cheg)
