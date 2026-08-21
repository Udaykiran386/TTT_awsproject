class Abs:
    def __new__(cls):
        print("constructor called")
        return super(Abs,cls).__new__(cls)
    def __init__(self):
        print("init called")

    def show(self):
        print("in Show")


obj1= Abs()
obj1.show()


obj2=Abs.__new__(Abs)
obj2.__init__
obj2.show()