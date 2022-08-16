class Area:
    def calculateArea(self,l,b):
        return l*b
    
class Areas:
    def calculateArea(self,r):
        return r*r*3.14
        
    


ob = Area()
print("area of rectangle is",ob.calculateArea(2,4))
ob1 = Areas()
print("area of circle is",ob1.calculateArea(2))

       