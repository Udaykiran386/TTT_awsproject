class computer:

    def __init__(self,name,message,speed,memory):
        print('hello i am init')
        self.name = name
        self.message = message
        self.speed = speed
        self.memory = memory
    name="i8"
    def config(self):
        print('my config: my name',self.name,self.message,self.speed,self.memory) 


com1=computer('i9','hello World!','speed 1 terahertz',"memory 1 Zettabyte")
com2=computer('i8','hello World!','speed 1/5 terahertz',"memory 1/5 Zettabyte")
print(computer.name)
print(com1.name)
com1.config()
com2.config()