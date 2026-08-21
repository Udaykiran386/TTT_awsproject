class laptop:
    model='i4'
    color='black'

    def __init__(self,model,color,name):
        self.model=model
        self.color=color
        self.name=name
        print('init')

    def show(self):
        print("in show "+self.name+" "+self.color+' '+self.model)


laptop1=laptop('i5','black','hp')
laptop1.show()