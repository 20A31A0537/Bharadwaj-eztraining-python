class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("Encap function-accesing protected")
        print(self._a+17)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)
#single underscore(_) represents protected
