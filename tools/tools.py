#Import Required Modules (for this valid the modules need to be built-in)
import random
import math

# Use Classes for diffrent solutions,
# Like for example, Randomtools for random stuff.
# We would be doing many updates, So you may need to make a new file with your functions
class Randomtools:
    def randfromlist(listhere):
        return listhere[random.randint(0,len(listhere)-1)]  
    def randfromcharstr(string):
        y = []
        for x in string:
            y.append(x)
        return y[random.randint(0,len(y)-1)]  
class Math:
    def frombin(b):
        power = len(b) - 1
        result = 0
        y = 0
        for x in b:
            y = y + 1
            if(x=="1"):
                result = result + 2**power 
            power = power - 1
        return result
    def tobin(integer):
        binary_string = ''
        while(integer > 0):
            digit = integer % 2
            binary_string += str(digit)
            integer = integer // 2
        binary_string = binary_string[::-1]
        return binary_string
    def avg(listofentries):
        y = 0
        c = 0
        for x in listofentries:
            try:
                y+=x
                c+=1
            except:
                print("One of the entries is not a number")
        return y/c
    def percent(first,second):
        D = first + second
        return [round(first/D*100,-1),round(second/D*100,-1)]
    class Geometry:
        def Circle(Rad):
            return round(math.pi * Rad**2)
        def Triangle(H,B):
            return round(1/2*B*H)
        def Square(X,Y):
            return X*Y
class Inp:
    def Intinput(prompt,Failprompt):
        try:
            x = int(input(str(prompt)))
            return x
        except:
            print(Failprompt)
    def MassCompare(lis,Value,Function):
        for x in lis:
            if Value == x:
                Function
                return [x,True]
        return [x,False]
class StrOp:
    def reverse(string):
        result = ''
        for x in string:
            result = x + result
        return result
    def getwords(string):
        # This is bugged so i made a placeholder to resolve this.
        string = string + ' Placeholder'
        yippie = ''
        result = []
        for x in string:
            if(x == ' '):
                result.append(yippie)
                yippie = ''
            else:
                yippie = yippie + x
        return result


