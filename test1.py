import time
from vscomputer import *
import pyttsx3
from tkinter import *
from pythoncolors import *
def disclaimer():
    dis=Tk()
    dis.geometry('1150x420')
    dis.configure(bg='black')
    Label(dis,text='DISCLAIMER',padx='100px',fg='yellow',bg='black',font='Jokerman 50 bold italic underline').grid()
    Label(dis,text='''
This game is made available by ANUNEET AND SHOURYA
\'s AUNEESOUR PRODUCTIONS.The sole purpose for the
work is to entertain the user by having him play this game.
This game is the modified version of THREE CARD FLASH.
The creators of the game (ANUNEET and SHOURYA) don\'t
personally endorse any type of gambling activities. ''',fg='red',bg='black',font='ravie 20 bold').grid()
    Button(dis,text='NEXT-->',fg='yellow',bg='black',font='forte 20 bold',command=dis.destroy).grid()
    dis.mainloop()

def Copyright():
    cop=Tk()
    cop.geometry('1160x520')
    cop.configure(bg='orange')
    Label(cop,text='COPYRIGHT ©',padx='50px',fg='yellow',bg='orange',font='Jokerman 60 bold italic underline').grid()
    Label(cop,text=('''
by (C) \' © 2020 \' ANUNEET AND SHOURYA

(AUNEESOUR HOME GAME PRODUCTIONS.)'''+str(chr(8482))+'''

ALL RIGHTS RESERVED.'''),fg='blue',bg='orange',font='ravie 30 bold').grid()
    Button(cop,text='QUiT',fg='yellow',bg='blue',font='forte 20 bold',command=cop.destroy).grid()
    cop.mainloop()

##Copyright()

def speak():
    engine=pyttsx3.init()
    engine.say('''Disclaimer!!!!
This game is made available by ANUNEET AND SHOURAYE
\'s ONEESOUR PRODUCTIONS. The sole purpose for the
work is to entertain the user by having him play this game.
This game is the modified version of THREE CARD FLASH.
The creators of the game (ANUNEET and SHOURaYe) don\'t
personally endorse any type of gambling activities.''' )
    engine.runAndWait()
#speak()
    
##disclaimer()


def hi():
    def rules():
        engine=pyttsx3.init()

        printc(green('*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*'))
        print()

        printc('1. '+ yellow('EVERY PLAYER WOULD BE GIVEN 13 RANDOM CARDS FROM THE CARD DECK.'))
        engine.say(' EVERY PLAYER WOULD BE GIVEN 13 RANDOM CARDS FROM THE CARD DECK.')
        engine.runAndWait()
        print()
        
        printc('2. ' + yellow('EACH PLAYER HAS TO MAKE 4 SETS OF CARDS HAVING 3 CARDS PER SET'))
        engine.say('EACH PLAYER HAS TO MAKE 4 SETS OF CARDS HAVING 3 CARDS PER SET') 
        engine.runAndWait()
        print()

        printc('3. ' + yellow('THE PRIORITY OF A SET IS CONCLUDED ON THE BASIS OF THE TYPE OF SET YOU HAVE MADE'))
        engine.say('THE PRIORITY OF A SET IS CONCLUDED ON THE BASIS OF THE TYPE OF SET YOU HAVE MADE')
        engine.runAndWait()
        print()

        printc(orange('*******************<--PRIORITY TABLE-->********************'))
        engine.say('priority table')
        engine.runAndWait()
        print()

        printc(purple('THREE OF A KIND ( TRIPLETS ) HAS THE HIGHEST PRIORITY'))
        engine.say('THREE OF A KIND ( TRIPLETS ) HAS THE HIGHEST PRIORITY')
        engine.runAndWait()
        print()
        
        printc('' + blue('PRIORITY OF TRIPLETS AAA,KKK,QQQ,JJJ,101010,999,888,777,666,555,444,333,222'))
        engine.say('PRIORITY OF TRIPLETS is as follows')
        engine.runAndWait()
        print()
        
        printc('' + purple('DOUBLE SEQUENCE SEQUENCE OF SAME GROUP i.e. SPADES,etc. EXAMPLE A')+black('♠')+purple('K')+(black('♠')+purple('Q')+black('♠')+purple('COMES SECOND ON PRIORITY SERIES AFTER TRIPLETS')))
        engine.say('DOUBLE SEQUENCE SEQUENCE OF SAME GROUP that is SPADES , etcetra . COMES SECOND ON PRIORITY SERIES AFTER TRIPLETS')
        engine.runAndWait()
        print()
        
        printc('' + blue('PRIORITY OF DOUBLE SEQUENCES AKQ,A23,KQJ,10JQ,9(10)J,89(10),789,678,567,456,345,234'))
        engine.say('PRIORITY OF DOUBLE SEQUENCES is as follows')
        engine.runAndWait()
        print()

        printc('' + purple('SINGLE SEQUENCE SEQUENCE OF DIFFERENT GROUP, EXAMPLE A') + black('♠') + purple('K') + black('♣') + purple('Q') + red('♥') +purple("COMES THIRD ON PRIORITY SERIES AFTER DOUBLE SEQUENCE"))
        engine.say('SINGLE SEQUENCE SEQUENCE OF DIFFERENT GROUP, COMES THIRD ON PRIORITY SERIES AFTER DOUBLE SEQUENCE')
        engine.runAndWait()
        print()
        
        printc('' + blue('PRIORITY OF SINGLE SEQUENCES AKQ,A23,KQJ,10JQ,9(10)J,89(10),789,678,567,456,345,234'))
        engine.say('PRIORITY OF SINGLE SEQUENCES is as follows')
        engine.runAndWait()
        print()
        
        printc('' + purple('THEN COMES COLOR WHICH IS A SET THAT HAVE A NON-SEQUENCE OF SAME GROUP EXAMPLE A')+black('♠')+purple('K')+black('♠')+purple('J')+black('♠'))
        engine.say('THEN COMES COLOR WHICH IS A SET THAT HAVE A NON-SEQUENCE OF SAME GROUP')
        engine.runAndWait()
        print()
        
        printc('' + blue('PRIORITY OF SINGLE SEQUENCES AKQ,A23,KQJ,10JQ,9(10)J,89(10),789,678,567,456,346,235,ETC....'))
        engine.say('PRIORITY OF SINGLE SEQUENCES is as follows')
        engine.runAndWait()
        print()
        
        printc('' + purple('THEN COMES DOUBLETS WITH TWO OF A KIND EXAMPLE A')+black('♠')+purple('A')+black('♣')+purple('K')+black('♣'))
        engine.say('THEN COMES DOUBLETS WITH TWO OF A KIND')
        engine.runAndWait()
        print()
        
        printc('' + purple('LAST ARE SINGLETONS NEITHER SEQUENCE NOR COLOUR,EXAMPLE A') + black('♠') + purple('K') + red('♥') + purple('J') + black('♣') + purple('DIFFERENT GROUPS'))
        engine.say('LAST ARE SINGLETONS NEITHER SEQUENCE NOR COLOUR')
        engine.runAndWait()
        print()
        
        printc(orange('***************************************************************'))
        print()

        printc('' + green('MAKE SETS IN ACCORDANCE TO THESE RULES IN DESCENDING ORDER'))
        engine.say('MAKE SETS IN ACCORDANCE TO THESE RULES IN DESCENDING ORDER')
        engine.runAndWait()
        print()
        
        printc('' + yellow('HOPE THIS HELPED YOU...........................'))
        engine.say('HOPE THIS HELPED YOU')
        engine.runAndWait()
        print(':) ;) :) ;):) ;) :) ;):) ;) :) ;):) ;) :) ;):) ;) :) ;):) ;) :) ;):) ;) :) ;):) ;) :) ;):) ;) :) ;)')
        print()
        
        hello.destroy()
##    def window():
##        hello.destroy()
##        def vscom():
##            vscomputer()
##        def ga():
##            game()
##        hell=Tk()
##        hell.geometry('100x100')
##        hell.configure(bg='black')
##        hell.title('let\'s play')
##        Button(hell,text='VS FRIENDS',fg='gold',bg='black',font='forte 30 bold',command=game).grid()
##        Button(hell,text='VS COMPUTER',fg='gold',bg='black',font='forte 30 bold',command=vscomputer).grid()
##        hell.mainloop()
    hello=Tk()
    hello.geometry('680x600')
    hello.configure(bg='black')
    hello.title('let\'s play')
    engine=pyttsx3.init()
    Label(hello,text=' Anuneet   and   Shourya   Presents ',fg='orange',bg='purple',font='Magneto 25 bold italic').grid(row=0,column=1)
    engine.say('   Anuneet.....;   and   Shouraye   Presents.... ')
    engine.say('.....AN ONEESOUR..; HOME GAME PRODUCTIONS....')
    engine.say(' A.. PYTHON. ORIGINALSS GAME ')
    engine.runAndWait()
    Label(hello,text='    13     ',fg='purple',bg='violet',font='Jokerman 150 bold').grid(row=1,column=1)
    engine.say('13 CARD!')
    engine.runAndWait()
    Label(hello,text='          CARD FLASH          ',fg='orange',bg='purple',font='Ravie 30 bold').grid(row=2,column=1)
    engine.say(' ;: FLASH')
    engine.runAndWait()
    Button(hello,text='RULES',fg='gold',bg='black',font='forte 30 bold',command=rules).grid(row=3,column=1)
    Button(hello,text='LET\'S PLAY 13 Patti',fg='gold',bg='black',font='forte 30 bold',command=hello.destroy).grid(row=4,column=1)
    hello.mainloop()

#hi()

def password():
    def x():
        return y.get()
    Root=Tk()
    y=StringVar()
    Root.title('ENTER YOUR PASSWORD')
    Root.configure(bg='aqua')
    Label(Root,text='Password: ',fg='blue',bg='aqua',font='Forte 30 bold').grid(row=1,column=0)
    ps=Entry(Root,textvariable=y,fg='yellow',bg='blue',font='Ravie 30 bold',show='*')
    ps.grid(row=1,column=1)
    Button(Root,text='submit',fg='yellow',bg='darkblue',font='Forte 16',command=Root.destroy).grid(row=2,column=1)
    Root.mainloop()
    return x()

#password()

def userpass():
    def c():
        return g.get(),h.get()
    root=Tk()
    h=StringVar()
    g=StringVar()
    root.configure(bg='aqua')
    root.title('ENTER YOUR DETAILS')
    
    Label(root,text='Username: ',fg='blue',bg='aqua',font='Forte 30 bold').grid(row=0,column=0)
    user=Entry(root,textvariable=g,fg='yellow',bg='blue',font='Stencil 30 bold')
    user.grid(row=0,column=1)

    Label(root,text='Password: ',fg='blue',bg='aqua',font='Forte 30 bold').grid(row=1,column=0)
    pas=Entry(root,textvariable=h,fg='yellow',bg='blue',font='Ravie 23 bold',show='*')
    pas.grid(row=1,column=1)

    Button(root,text='submit',fg='yellow',bg='darkblue',font='Forte 16',command=root.destroy).grid(row=2,column=1)
    root.mainloop()
    return c()

#userpass()

##def suit():
##    def Z():
##        return(z.get())
##    sp=Tk()
##    z=StringVar()
##    z.set(chr(9824))
##    Label(sp,text='♠',font='Forte 30 bold').grid(row=1,column=0)
##    Label(sp,text='♣',font='Forte 30 bold').grid(row=2,column=0)
##    Label(sp,text='♥',font='Forte 30 bold').grid(row=3,column=0)
##    Label(sp,text='♦',font='Forte 30 bold').grid(row=4,column=0)
##    Radiobutton(sp,text='PRESS TO INSERT SPADES',variable=z,value=chr(9824)).grid(row=1,column=1)
##    Radiobutton(sp,text='PRESS TO INSERT CLUBS',variable=z,value=chr(9827)).grid(row=2,column=1)
##    Radiobutton(sp,text='PRESS TO INSERT HEARTS',variable=z,value=chr(9829)).grid(row=3,column=1)
##    Radiobutton(sp,text='PRESS TO INSERT DIAMONDS',variable=z,value=chr(9830)).grid(row=4,column=1)
##    Button(sp,text='OK',command=sp.destroy).grid(row=5,column=0)
##    sp.mainloop()
##    return Z()

count=4
coun=0
ab=0
Xi=[]
B=[]
def sets(bi):
    global Xi
    Xi=[]
    ch=Tk()
    ch.geometry('950x600')
    ch.configure(bg='#ff3399')
    M=StringVar()
    N=StringVar()
    O=StringVar()
    P=StringVar()
    Label(ch,text='SET 1-> ',fg='gold',bg='#ff3399',font='Stencil 25 bold').grid(row=0,column=0)
    Entry(ch,textvariable=M,fg='blue',bg='gold',font='jokerman 20 bold',width=10).grid(row=0,column=1)
    Label(ch,text='hint:choose 3 highest cards',fg='gold',bg='#ff3399',font='Stencil 25 bold').grid(row=0,column=2)

    Label(ch,text='SET 2-> ',fg='yellow',bg='#ff3399',font='Stencil 25 bold').grid(row=1,column=0)
    Entry(ch,textvariable=N,fg='blue',bg='yellow',font='jokerman 20 bold',width=10).grid(row=1,column=1)
    Label(ch,text='hint:second 3 highest cards',fg='yellow',bg='#ff3399',font='Stencil 25 bold').grid(row=1,column=2)
        
    Label(ch,text='SET 3-> ',fg='purple',bg='#ff3399',font='Stencil 25 bold').grid(row=2,column=0)
    Entry(ch,textvariable=O,fg='yellow',bg='purple',font='jokerman 20 bold',width=10).grid(row=2,column=1)
    Label(ch,text='hint:third 3 highest cards  ',fg='purple',bg='#ff3399',font='Stencil 25 bold').grid(row=2,column=2)
        
    Label(ch,text='SET 4-> ',fg='darkblue',bg='#ff3399',font='Stencil 25 bold').grid(row=3,column=0)
    Entry(ch,textvariable=P,fg='gold',bg='darkblue',font='jokerman 20 bold',width=10).grid(row=3,column=1)
    Label(ch,text='hint:choose 3 lowest cards  ',fg='darkblue',bg='#ff3399',font='Stencil 25 bold').grid(row=3,column=2)
        
    def button(J):
        global count,coun
        def D():
            global ab
            ab+=1
            if ab<4:
                M.set(J+','+M.get())
            elif ab<7:
                N.set(J+','+N.get())
            elif ab<10:
                O.set(J+','+O.get())
            elif ab<13:
                P.set(J+','+P.get())
            F['state']=DISABLED
        if J[-1] in ['♥','♦']:
            if count<8:
                F=Button(ch,text=J,fg='white',bg='red',font='ravie 20 bold',command=D,width=2,height=1)
                F.grid(row=count,column=0)
                count+=1
            elif 8<=count and count<12:
                F=Button(ch,text=J,fg='white',bg='red',font='ravie 20 bold',command=D,width=2,height=1)
                F.grid(row=(count-4),column=1)
                count+=1
            else:
                F=Button(ch,text=J,fg='white',bg='red',font='ravie 20 bold',command=D,width=2,height=1)
                F.grid(row=(count-8),column=2)
                count+=1
        else:
            if count<8:
                F=Button(ch,text=J,fg='white',bg='black',font='ravie 20 bold',command=D,width=2,height=1)
                F.grid(row=count,column=0)
                count+=1
            elif 8<=count and count<12:
                F=Button(ch,text=J,fg='white',bg='black',font='ravie 20 bold',command=D,width=2,height=1)
                F.grid(row=(count-4),column=1)
                count+=1
            else:
                F=Button(ch,text=J,fg='white',bg='black',font='ravie 20 bold',command=D,width=2,height=1)
                F.grid(row=(count-8),column=2)
                count+=1
        return F
    for J in bi:
        A=button(J)
        Xi.append(A)
    def tryc():
        global ab,Xi
        for K in Xi:
            K['state']=NORMAL
            M.set('')
            N.set('')
            O.set('')
            P.set('')
            ab=0

    def see():
        global B
        B=[M.get().rstrip(',').split(','),N.get().rstrip(',').split(','),O.get().rstrip(',').split(','),P.get().rstrip(',').split(',')]
        
        ch.destroy()
            
    Q=Button(ch,text='RESET',fg='lime',bg='blue',font='forte 24 bold',command=tryc,width=10)
##    Q.grid()
    Q.grid(row=9,column=0)
    Q=Button(ch,text='SUBMiT',fg='lime',bg='blue',font='forte 24 bold',command=see,width=10)
    Q.grid(row=9,column=1)
##    Q.grid()
    ch.mainloop()
    global ab,coun,count
    ab=0
    coun=0
    count=4
    return B

##sets(['a@','s#','d#','f@','g#','h@','j@','k@','l#','q#','w@','t@','e#','r#'])
def inorder(b):
    u=list('AKQJ198765432')
    d={}
    c1=[]
    c2=[]
    c11=[]
    c12=[]
    co=0
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
        c2.append(d[i1])
    return c2










            
