class Cars:
    # constructor
    def __init__(self,type,color,model):
        self.type=type
        self.color= color
        self.model=model

        # method

    def onyesha(self):
        print(f"I love {self.model} cars which is a {self.type} being {self.color}")


#   creating an object

myobj = Cars("Saloon","white","Toyota")
myobj.onyesha()
my0bj2=Cars("S.Wagon","Black","Benz")
my0bj2.onyesha()
