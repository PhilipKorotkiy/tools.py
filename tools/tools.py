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
        def Trapiziod(top,bottom,height):
            return 1/2*(top+bottom)*height
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
    def letterindex(letter):
        return ord(letter.lower()) - 97
    def indextoletter(pos):
        return chr(pos + 97)
    def reverse(string):
        result = ''
        for x in string:
            result = x + result
        return result
    def getwords(string,Separator):
        # This is bugged so i made a placeholder to resolve this.
        string = string + ' Placeholder'
        yippie = ''
        result = []
        for x in string:
            if(x == Separator):
                if yippie != '':
                    result.append(yippie)
                yippie = ''
            elif(x != '.' and x != '?' and x != '!'and x != ',' and x != '"' and x != "'" ):
                yippie = yippie + x
        return result
    def reversewords(string):
        # This is bugged so i made a placeholder to resolve this.
        string = string + ' Placeholder'
        yippie = ''
        ending = ''
        result = []
        i = 0
        for x in string:
            if(x == ' '):
                result.append(yippie)
                yippie = ''
            else:
                yippie = yippie + x
        result.reverse()
        for x in result:
            if i == 0:
                ending = x
            else:
                ending = ending + ' ' +x
            i += 1
        return ending
    def ShiftEncode(string,shift):
        final = ''
        string = string.lower()
        for x in string:
            if (x != ' ' and x != '.' and x != ',' and x != '/'):
                z = StrOp.letterindex(x) + shift
                if(z >= 25): 
                    y = StrOp.indextoletter(z - 25)
                else:
                    y = StrOp.indextoletter(z)
            else:
                y = x
            final = final + y
        return final
    def ShiftDecode(code,shift):
        result = ''
        for x in code:
            if x != ' ' and x != ',' and x != '.' and x != '/':
                z = StrOp.letterindex(x) - shift
                if z <= -1:
                    y = StrOp.indextoletter(z + 25)
                else:
                    y = StrOp.indextoletter(z)
            else:
                y = x
            result = result + y
        return result

