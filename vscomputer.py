from compare import *
import random
types='troy double run color pair highcards'.split()
card=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
cards=[]
for i in ['♠','♣','♥','♦']:
    for j in card:
        cards+=[(j+i)]
b=[]
for l in range(13):
            c=random.choice(cards)
            b+=[c]
            cards.pop(cards.index(c))

##b=['4♦', 'Q♠', 'Q♦', '4♥', '2♠', 'A♠', '10♥', 'Q♣', '8♥', '7♠', '4♣', '9♥', '3♣']
##b=['A♠', 'A♣', 'K♦', 'K♣', '7♠', '6♦', '5♠', '5♥', '4♥', '3♣', '3♥', '2♥', 'A♥']
##b=['A♣', 'A♦', 'K♥', 'Q♣', 'Q♦', 'J♣', '10♥', '10♣', '9♥', '7♠', '6♥', '4♣', '2♠']


def vscomputer(b):
    u=list('AKQJ198765432')
    d={} # getting corresponding value as in u(index according to cards)
    c1=[] # having index of card first character for sorting
    c2=[] #having corresponding suit of cards
    c11=[]#getting sorted list of cards
    co=0 # for special case if same cards(but different suit) are in list of card

    for i in range(13):
        if (u.index(b[i][0]),) in c1:
            d[(u.index(b[i][0]),chr(96+co))]=b[i]
            c1.append((u.index(b[i][0]),chr(96+co)))
            co+=1
        else:
            c1.append((u.index(b[i][0]),))
            d[(u.index(b[i][0]),)]=b[i]
    c1.sort()
    for i1 in c1:
        c2.append(d[i1][-1])
        c11.append(d[i1])
    for i2 in range(13):
        c1[i2]=c1[i2][0]
    print(c11)
    for i in range(13):
        if c11[i][0]=='1':
            c11[i]=c11[i][0]+c11[i][-1]

    los=[] #list of set
    counter=0 #for replacement of removed cards so that index does not change
    set_formed=[]
    while counter<12:
        for index in range(len(c1)):
            set1=[]
            if c1.count(c1[index])>=3: #for if cards having troy
                los.append(['troy',c1[index]])

                counter+=1
                c1.pop(index)
                c1.insert(index,chr(96+counter))
                set1.append(c11[index])
                c11.pop(index)
                c11.insert(index,chr(96+counter))
                c2.pop(index)
                c2.insert(index,chr(96+counter))
                counter+=1
                c1.pop(index+1)
                c1.insert(index+1,chr(96+counter))
                set1.append(c11[index+1])
                c11.pop(index+1)
                c11.insert(index+1,chr(96+counter))
                c2.pop(index+1)
                c2.insert(index+1,chr(96+counter))
                counter+=1
                c1.pop(index+2)
                c1.insert(index+2,chr(96+counter))
                set1.append(c11[index+2])
                c11.pop(index+2)
                c11.insert(index+2,chr(96+counter))
                c2.pop(index+2)
                c2.insert(index+2,chr(96+counter))

                set_formed.append(set1)
        for index in range(len(c1)):
            set1=[]
    ##        print(type(c1[index])==type(3),(c1[index]+1 in c1),(c1[index]+2 in c1),(u[c1[index]+1]+c2[index] in c11),(u[c1[index]+2]+c2[index] in c11))
            if type(c1[index])==type(3) and(c1[index]+1 in c1) and (c1[index]+2 in c1)and(u[c1[index]+1]+c2[index] in c11)and(u[c1[index]+2]+c2[index] in c11):
                m,n,c=(index,c11.index(u[c1[index]+1]+c2[index]),c11.index(u[c1[index]+2]+c2[index]))
                los.append(['double',(c1[index],c1[index]+1,c1[index]+2)])

                counter+=1
                c1.pop(m)
                c1.insert(m,chr(96+counter))
                set1.append(c11[m])
                c11.pop(m)
                c11.insert(m,chr(96+counter))
                c2.pop(m)
                c2.insert(m,chr(96+counter))
                counter+=1
                c1.pop(n)
                c1.insert(n,chr(96+counter))
                set1.append(c11[n])
                c11.pop(n)
                c11.insert(n,chr(96+counter))
                c2.pop(n)
                c2.insert(n,chr(96+counter))
                counter+=1
                c1.pop(c)
                c1.insert(c,chr(96+counter))
                set1.append(c11[c])
                c11.pop(c)
                c11.insert(c,chr(96+counter))
                c2.pop(c)
                c2.insert(c,chr(96+counter))

                set_formed.append(set1)
            elif type(c1[index])==type(3) and (c1[index]==0) and (11 in c1) and (12 in c1)and('2'+c2[index] in c11)and('3'+c2[index] in c11):
                m,n,c=(index,c11.index('2'+c2[index]),c11.index('3'+c2[index]))
##                print(c11.index('3'+c2[index]))
                los.append(['double',(c1[index],11,12)])

                counter+=1
                c1.pop(m)
                c1.insert(m,chr(96+counter))
                set1.append(c11[m])
                c11.pop(m)
                c11.insert(m,chr(96+counter))
                c2.pop(m)
                c2.insert(m,chr(96+counter))
                counter+=1
                c1.pop(n)
                c1.insert(n,chr(96+counter))
                set1.append(c11[n])
                c11.pop(n)
                c11.insert(n,chr(96+counter))
                c2.pop(n)
                c2.insert(n,chr(96+counter))
                counter+=1
                c1.pop(c)
                c1.insert(c,chr(96+counter))
                set1.append(c11[c])
                c11.pop(c)
                c11.insert(c,chr(96+counter))
                c2.pop(c)
                c2.insert(c,chr(96+counter))

                set_formed.append(set1)
        for index in range(len(c1)):
            set1=[]
    ##        xprint(type(c1[index])==type(3) and(c1[index]+1 in c1) and (c1[index]+2 in c1))
            if type(c1[index])==type(3) and(c1[index]+1 in c1) and (c1[index]+2 in c1) :
                m,n,c=(c1.index(c1[index]),c1.index(c1[index]+1),c1.index(c1[index]+2))
                los.append(['run',(c1[index],c1[index]+1,c1[index]+2)])

                counter+=1
                c1.pop(m)
                c1.insert(m,chr(96+counter))
                set1.append(c11[m])
                c11.pop(m)
                c11.insert(m,chr(96+counter))
                c2.pop(m)
                c2.insert(m,chr(96+counter))
                counter+=1
                c1.pop(n)
                c1.insert(n,chr(96+counter))
                set1.append(c11[n])
                c11.pop(n)
                c11.insert(n,chr(96+counter))
                c2.pop(n)
                c2.insert(n,chr(96+counter))
                counter+=1
                c1.pop(c)
                c1.insert(c,chr(96+counter))
                set1.append(c11[c])
                c11.pop(c)
                c11.insert(c,chr(96+counter))
                c2.pop(c)
                c2.insert(c,chr(96+counter))
                set_formed.append(set1)
            elif type(c1[index])==type(3) and (c1[index]==0) and (11 in c1) and (12 in c1) :
                m,n,c=(c1.index(c1[index]),c1.index(11),c1.index(12))
                los.append(['run',(c1[index],11,12)])

                counter+=1
                c1.pop(m)
                c1.insert(m,chr(96+counter))
                set1.append(c11[m])
                c11.pop(m)
                c11.insert(m,chr(96+counter))
                c2.pop(m)
                c2.insert(m,chr(96+counter))
                counter+=1
                c1.pop(n)
                c1.insert(n,chr(96+counter))
                set1.append(c11[n])
                c11.pop(n)
                c11.insert(n,chr(96+counter))
                c2.pop(n)
                c2.insert(n,chr(96+counter))
                counter+=1
                c1.pop(c)
                c1.insert(c,chr(96+counter))
                set1.append(c11[c])
                c11.pop(c)
                c11.insert(c,chr(96+counter))
                c2.pop(c)
                c2.insert(c,chr(96+counter))

                set_formed.append(set1)
        for index in range(len(c1)):
            set1=[]
            if c2.count(c2[index])>=3: #for if cards having color
                a=c2[index]
                m=c2.index(a)
                b=(c1[m],)
                counter+=1
                c1.pop(m)
                c1.insert(m,chr(96+counter))
                set1.append(c11[m])
                c11.pop(m)
                c11.insert(m,chr(96+counter))
                c2.pop(m)
                c2.insert(m,chr(96+counter))
                counter+=1
                
                
                m=c2.index(a)
                b+=(c1[m],)
                c1.pop(m)
                c1.insert(m,chr(96+counter))
                set1.append(c11[m])
                c11.pop(m)
                c11.insert(m,chr(96+counter))
                c2.pop(m)
                c2.insert(m,chr(96+counter))
                counter+=1

                m=c2.index(a)
                b+=(c1[m],)
                c1.pop(m)
                c1.insert(m,chr(96+counter))
                set1.append(c11[m])
                c11.pop(m)
                c11.insert(m,chr(96+counter))
                c2.pop(m)
                c2.insert(m,chr(96+counter))
                counter+=1
                

                los.append(['color',b])
                set_formed.append(set1)
        for index in range(len(c1)):
            set1=[]
            b=0
            if c1.count(c1[index])==2: #for if cards having color
                m=index

                counter+=1
                set1.append(c11[m])
                c11.pop(m)
                c11.insert(m,chr(96+counter))
                c2.pop(m)
                c2.insert(m,chr(96+counter))
                c1.pop(m)
                c1.insert(m,chr(96+counter))

                counter+=1
                set1.append(c11[m+1])
                c11.pop(m+1)
                c11.insert(m+1,chr(96+counter))
                c2.pop(m+1)
                c2.insert(m+1,chr(96+counter))
                c1.pop(m+1)
                c1.insert(m+1,chr(96+counter))
                
                for ele in c1:
                    if type(ele)==type(2):
                        ind=c1.index(ele)
##                        print(ind)
                        break
                counter+=1
                c1.pop(c1.index(c1[ind]))
                c1.insert(c1.index(c1[ind]),chr(96+counter))
                set1.append(c11[ind])
                
                c11.pop(c1.index(c1[ind]))
                c11.insert(c1.index(c1[ind]),chr(96+counter))
                c2.pop(c1.index(c1[ind]))
                c2.insert(c1.index(c1[ind]),chr(96+counter))

                los.append(['pair',(index,ind,index)])
                set_formed.append(set1)
        b=()
        c=0
        set1=[]
        for index in range(13):
            
            if type(c1[index])==type(2):
                c+=1
                b+=(c1[index],)
                counter+=1
                set1.append(c11[index])
                c11.pop(index)
                c11.insert(index,chr(96+counter))
                c2.pop(index)
                c2.insert(index,chr(96+counter))
                c1.pop(index)
                c1.insert(index,chr(96+counter))
                if c==3:
                    los.append(['highcards',b])
                    set_formed.append(set1)
                    set1=[]
                    c=0;b=()

##    print(c1,c2,c11)
    
    for i in set_formed:
        for j in i:
            if j[0]=='1':
                i[i.index(j)]='10'+j[-1]
    print(set_formed)
    flos=[]
    print(los)
    return los
##a=vscomputer(b)
##d={'computer':a,'b':a}
##print(a)
##print(last(d))
