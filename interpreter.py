F=["f"]
Fd=[lambda x,y: x+y,lambda x,y: x-y,lambda x,y: x*y,lambda x,y: x/y, lambda x,y: x**y,lambda x,y: x**(1/y)]
class Token:
    def __init__(self,v,n,t):
        self.Value=v
        self.Name=n
        self.Type=t


def debug(r):
    print(r)
    for i in r:
        print(i.Value,i.Name,i.Type)


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


def Calc(tok):
    i=0
    while i < len(tok):
        if tok[i].Type=="Assignation":
            if i+1<len(tok):
                if tok[i+1].Type=="Operator":
                    ff=int(tok[i+1].Value)
                    tok.insert(i+1,Token(Fd[ff](int(tok[i].Value),int(tok[i+2].Value)),tok[i].Name,"Assignation"))
                    tok.remove(tok[i])
                    tok.remove(tok[i+1])
                    tok.remove(tok[i+1])
                    i-=1
                    pass
        i+=1
    return tok

c="a2f0b7f1c2f2d2f2e2f4e2f4e2"
result=Analyser(c)
result=Calc(result)


"""for i in range(len(result)):
    if result[i].Type=="Operator":
        ff=int(result[i].Value)
        print(Fd[ff](int(result[i-1].Value),int(result[i+1].Value)))"""

#debug(result)
print(result[0].Value)

"""

Example to understand the writing method:

'a2f0b7' -> any letters a the beginning define a new var with an
integer, only from 0 to 9 and the letter f is for 'Function',
there is 2 function right now, f0 if to add the token before and after
and f2 is to minus the token before and after

Class Token -> A token contains the value and the type for each caracters
Analyser Func -> analyse the func (i don't want to explain)

that's all for me, have a good day

"""