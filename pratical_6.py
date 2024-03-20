def stateq0(n):
    if(len(n) == 0 ):
        print("String Accepted")
    else:
        if(n[0] == '0'):
            stateq0(n[1:])
        elif(n[0] == '1'):
            stateq1(n[1:])
def stateq1(n):
    if(len (n)==0):
        print("String not Accepted")
    else:
        if(n[0] == '0'):
            stateq0(n[1:])
        elif(n[0] == '1'):
            stateq1(n[1:])
n = int(input("Enter number : "))
n = bin(n).replace("0b" ,"")
stateq0(n)
