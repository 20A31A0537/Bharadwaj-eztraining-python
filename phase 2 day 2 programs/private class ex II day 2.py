class encap:
    __a=10
    print(__a+15)
    def encapfunction(self):
        _b=200
        print("Encap function-accesing protected")
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj._a)
#double underscore(__) represents private variable
