from idlecolors import *
u=list('AKQJ198765432')
types='troy double run color pair highcards'.split()
v=[]
j=[]
def compared(b):
    f=b
    def sorting(a):
        global u,v,j,types
        j=[]
        
        for i in range(4):
            p,q,r=a[i][0],a[i][1],a[i][2]
            l=f'{u.index(p[0])}a'
            m=f'{u.index(q[0])}b'
            n=f'{u.index(r[0])}c'
            if p[0]==q[0] or p[0]==r[0] or q[0]==r[0]:
                v.append(l)
                v.append(m)
                v.append(n)
                
            else:
                v.append(u.index(p[0]))
                v.append(u.index(q[0]))
                v.append(u.index(r[0]))
            d={v[0]:p,v[1]:q,v[2]:r}
            v.sort()
            z=[d[v[0]],d[v[1]],d[v[2]]]
            j.append(z)
            v=[]
        return j
    f=sorting(f)
    for i in f:
        x=i[0];p=u.index(x[0])
        y=i[1];q=u.index(y[0])
        z=i[2];r=u.index(z[0])
        if x[0]==y[0]==z[0]:
            f[f.index(i)].append(['troy',p])
        elif (x[-1]==y[-1] and y[-1]==z[-1])and(q==p+1 and r==q+1):
            f[f.index(i)].append(['double',(p,q,r)])
        elif (p==0 and q==11 and r==12)and(x[1]==y[1]==z[1]):
            f[f.index(i)].append(['double',(p,q,r)])
        elif (q==p+1 and r==q+1):
            f[f.index(i)].append(['run',(p,q,r)])
        elif (p==0 and q==11 and r==12):
            f[f.index(i)].append(['run',(p,q,r)])
        elif (x[-1]==y[-1]==z[-1]):
            f[f.index(i)].append(['color',(p,q,r)])
        elif (x[0]==y[0])or(x[0]==z[0])or(y[0]==z[0]):
            if (x[0]==y[0]):
                f[f.index(i)].append(['pair',(p,r,q)])
            elif (y[0]==z[0]):
                f[f.index(i)].append(['pair',(q,p,r)])
            elif (z[0]==x[0]):
                f[f.index(i)].append(['pair',(p,q,r)])
        else:
            f[f.index(i)].append(['highcards',(p,q,r)])
    new=[]
    fx=[]
    dic={}
    cd=0
    for i in f:
        a=i[-1]
        b=types.index(a[0])
        if str(b) in new:
            cd+=1
            dic[str(b)+chr(96+cd)]=i
            new.append(str(b)+chr(96+cd))
        else:
            dic[str(b)]=i
            new.append(str(b))
    new.sort()
    
    for j in new:
        fx.append(dic[j])
    def exsort(fx):
        global types
        llist=[]
        aw,ax,ay,az=fx[0][-1],fx[1][-1],fx[2][-1],fx[3][-1]
        mn=[[types.index(aw[0]),aw[1]],[types.index(ax[0]),ax[1]],[types.index(ay[0]),ay[1]],[types.index(az[0]),az[1]]]
        mn.sort()
        
        for i in mn:
            asd=[types[i[0]],i[1]]
            llist.append(asd)
        return llist
    a=exsort(fx)
    return a
def last(s):
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    for i in s.keys():
        a=s[i]
        l1.append([types.index(a[0][0]),a[0][1]])
        l2.append([types.index(a[1][0]),a[1][1]])
        l3.append([types.index(a[2][0]),a[2][1]])
        l4.append([types.index(a[3][0]),a[3][1]])
    m1=sorted(l1)
    m2=sorted(l2)
    m3=sorted(l3)
    m4=sorted(l4)
    kl=list(s.keys())
    if l1.count(m1[0])>1:
        for i in l1:
            if l1.count(m1[0])==1:
                pass
            else:
                s1=l1.index(m1[0])
                l1.pop(s1)
                l1.insert(s1,'abc')
        win1=kl[l1.index(m1[0])]
    else:
        show1=l1.index(m1[0])
        win1=list(s.keys())[l1.index(m1[0])]
    
    if l2.count(m2[0])>1:
        l2=l2[show1:]+l2[:show1]
        kl=kl[show1:]+kl[:show1]
        for i in l2:
            if l2.count(m2[0])==1:
                break
            else:
                s2=l2.index(m2[0])
                l2.pop(s2)
                l2.insert(s2,'abc')
        show2=l2.index(m2[0])
        win2=kl[l2.index(m2[0])]
    else:
        show2=l2.index(m2[0])
        win2=list(s.keys())[l2.index(m2[0])]
    
    if l3.count(m3[0])>1:
        l3=l3[show2:]+l3[:show2]
        kl=kl[show2:]+kl[:show2]
        for i in l3:
            if l3.count(m3[0])==1:
                pass
            else:
                s3=l3.index(m3[0])
                l3.pop(s3)
                l3.insert(s3,'abc')
        show3=l3.index(m3[0])
        win3=kl[l3.index(m3[0])]
    else:
        show3=l3.index(m3[0])
        win3=list(s.keys())[l3.index(m3[0])]
    
    if l4.count(m4[0])>1:
        l4=l4[show3:]+l4[:show3]
        kl=kl[show3:]+kl[:show3]
        for i in l4:
            if l4.count(m4[0])==1:
                pass
            else:
                s4=l4.index(m4[0])
                l4.pop(s4)
                l4.insert(s4,'abc')
        win4=kl[l4.index(m4[0])]
    else:
        win4=list(s.keys())[l4.index(m4[0])]

    return(win1,win2,win3,win4)

def scoreboard(a,d):
    printc(green('*************************SCOREBOARD**************************'))
    f1={}
    for i in d.keys():
        
        printc(red('player name is ')+yellow(str(i)))
        a1=a.count(i)
        if a1==4:
            printc(orange('player points are ')+purple(str(a1*25+50)))
        else:
            printc(orange('player points are ')+purple(str(a1*25)))
        if a1==0:
            printc(blue('set win by ')+green(str(i))+blue(' are ')+yellow('None'))
        else:
            printc(blue('set win by ')+green(str(i))+blue(' are '))
            print('\t')
            for j in range(4):
                if a[j]==i:
                    printc(yellow('set '+str(j+1)))
        f1[i]=[d[i][1],a1*25]
    return f1
