#method overloading
class moverload:
    def display(self,a=None,b=None):
        print(a,b)
obj=moverload()
print("without arguments")
obj.display()
print("with arguments")
obj.display(25,27)
print("with one argument")
obj.display(25)
