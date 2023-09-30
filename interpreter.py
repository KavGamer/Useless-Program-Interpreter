F=["f"]
Fd=[lambda x,y: x+y,lambda x,y: x-y]
class Token:
    def __init__(self,v,n,t):
        self.Value=v
        self.Name=n
        self.Type=t

def Analyser(source):  
    p=0
    tokens=[]
    while p<len(source):
        if not(source[p] in F):
            if not(source[p].isdigit()):
                tokens.append(Token(source[p+1],source[p],"Assignation"))
        else:
            tokens.append(Token(source[p+1],F.index(source[p]),"Operator"))

        p=p+1
    return tokens


c="a2f0b7"
result=Analyser(c)


"""print(result)
for i in result:
    print(i.Value,i.Name,i.Type)"""


for i in range(len(result)):
    if result[i].Type=="Operator":
        ff=int(result[i].Value)
        print(Fd[ff](int(result[i-1].Value),int(result[i+1].Value)))


"""

Example to understand the writing method:

'a2f0b7' -> any letters a the beginning define a new var with an
integer, only from 0 to 9 and the letter f is for 'Function',
there is 2 function right now, f0 if to add the token before and after
and f2 is to minus the token before and after

Class Token -> A token contains the value and the type for each caracters
Analyser Func -> analyse the func (i don't want to explain)
Line 32-35 -> compile the different part of the source

that's all for me, have a good day

"""