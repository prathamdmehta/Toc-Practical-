def q1(s,i):
    print("q1->", end="")
    if (i == len(s)):
        print("NO")
        return
    
    if(s[i] == "0"):
        q1(s, i+1)
    else: 
        q3(s, i+1)

def q2(s,i):
    print("q2->", end="")
    if (i == len(s)):
        print("NO")
        return
    
    if(s[i] == "0"):
        q4(s, i+1)
    else: 
        q2(s, i+1)

def q3(s,i):
    print("q3->", end="")
    if (i == len(s)):
        print("YES+")
        return
    
    if(s[i] == "0"):
        q4(s, i+1)
    else: 
        q2(s, i+1)


def q4(s,i):
    print("q4->", end="")
    if (i == len(s)):
        print("NO")
        return
    
    if(s[i] == "0"):
        q1(s, i+1)
    else: 
        q3(s, i+1)

def q0(s,i):
    print("q0->", end="")
    if (i == len(s)):
        print("NO")
        return
    
    if(s[i] == "0"):
        q1(s, i+1)
    else: 
        q2(s, i+1)

if __name__ == "__main__":
    s = "010101"
    print("State transitions are", end="")
    q0(s,0)
