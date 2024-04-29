
reg=[0,0,0]

def mov(a,b):
    print(a,b)
    p1=str(a).split("REG")
    p2=str(b).split("REG")
    if len(p1)==1:
        p1=int(p1[0])
    elif len(p1)==2:
        p1=reg[int(p1[1])]
    p2=int(p2[1])
    reg[p2]=p1
    print("reg:",reg)

def inc(a):
    reg[int(str(a).split("REG")[1])]+=1
    print("reg:",reg)

while True:
    action=input('>')
    action=action.split(' ')

    if action[0]=='MOV':
        mov(action[1],action[2])
    elif action[0]=="INC":
        inc(action[1])

    elif action[0]=="DEC":
        reg[int(action[1].split("REG")[1])]-=1

    elif action[0]=="ADD":
        p1=action[1].split("REG")
        p2=action[2].split("REG")
        if len(p1)==1:
            p1=int(p1[0])
        elif len(p1)==2:
            p1=reg[int(p1[1])]
        p2=int(p2[1])
        reg[p2]+=p1
    elif action[0]=="DO":
        p1=int(action[1])
        if len(action)==5:
            for x in range(p1):
                s=action[2].lower()+"("+action[3]+",'"+action[4]+"')"
                exec(str(s))
        elif len(action)==4:
            for x in range(p1):
                s=action[2].lower()+"('"+action[3]+"')"
                exec(str(s))


    print("reg:",reg)

"""
    MOV (REGx/int) REGy, x-->y
    INC REGx, REGx+=1
    DEC REGx, REGx-=1
    ADD REGx REGy, ( REGx + REGy ) --> y
    DO x; ..., do 'x' times ...

"""