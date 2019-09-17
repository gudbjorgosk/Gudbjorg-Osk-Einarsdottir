x,y = 1,1

def north(x,y): #function for north
    if y == 3 or (x,y) == (2,2) or (x,y) == (3,1):
        return False
    return True

def east(x,y): #function for not east
    if (x,y) != (1,2) and (x,y) != (1,3) and (x,y) != (2,3):
        return False
    return True

def west(x,y): #function for wwst
    if y == 1 or x == 1 or (x,y) == (3,2):
        return False
    return True

def south(x,y): #function for south
    if y == 1 or (x,y) == (2,3):
        return False
    return True

def string(n,e,s,w):
    dir = ""
    while dir == "":
        if n == True:
            dir += "(N)orth"
        elif e == True:
            dir += "(E)ast"
        elif s == True:
            dir += "(S)outh"
        elif w == True:
            dir += "(W)est"
    if e == True and dir != "(E)ast":
        dir += " or (E)ast"
    if s == True and dir != "(S)outh":
        dir += " or (S)outh"
    if w == True and dir != "(W)est":
        dir += " or (W)est"
    return dir
    
def which_way():
    i = input("Direction: ")
    i = i.upper()
    return i

def translocator(boolean):
    if boolean == True:
        return 1
    return 0

def move(x,y,string):
    if string == "N":
        y += translocator(N)
    elif string == "S":
        y -= translocator(S)
    elif string == "W":
        x -= translocator(W)
    elif string == "E":
        x += translocator(E)
    return x,y
    

while (x,y) != (3,1): #the victory is in (3,1)
    a = x
    b = y
    N,E,S,W = True,True,True,True
    N = north(x,y)
    E = east(x,y)
    S = south(x,y)
    W = west(x,y)
    directions = string(N,E,S,W)
    print("You can travel: " + directions + ".")
    command = ""
    while (x,y) == (a,b):
        command = which_way()
        x,y = move(x,y,command)
        if (x,y) == (a,b):
            print("Not a valid direction!")
print("Victory!")
