
class alphabets():
    def a (self):
        for row in range (7):
            for col in range (6):
                if((col==0 or col==5)and row!=0)or ((row==0 or row==3)and (col!=0 and col!=5)):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def b (self):
        for row in range (7):
            for col in range (6):
                if (col==0)or(col==5 and (row!=0 and row!=6))or((row==0 or row==3 or row==6)and col!=5):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def c (self):
        for r in range (7):
            for c in range (6):
                if(c==0 and (r!=0 and r!=6)) or ((r==0 or r==6) and (c!=0)):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def d (self):
        for r in range (7):
            for c in range (6):
                if ((c==0 or c==5)and (r!=0 and r!=6))  or ((r==0 or r==6) and (c!=5)):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def e (self):
        for r in range (7):
            for c in range (6):
                if (c==0)or (r==0 or r==6)or (r==3 and c!=5):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def f (self): 
        for r in range (7):
            for c in range (6):
                if (c==0 or r==0)or (r==3 and c!=5):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def g (self): 
        for r in range (7):
            for c in range (6):
                if (c==0 and (r!=0 and r!=6))or ((r==0 or r==6) and (c!=5 and c!=0))or(c==4 and (r>3 and r<6))or (r==3 and c>2)or(c==5 and r==1):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def h (self): 
        for r in range (7):
            for c in range (6):
                if (c==0 or c==5) or (r==3):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def i (self): 
        for r in range (7):
            for c in range (6):
                if ((r==0 or r==6)and c!=0)or (c==3):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def j (self): 
        for r in range (7):
            for c in range (6):
                if (r==0)or (c==3)or (r==4 and c==0)or (r==5 and c==1)or(c==2 and r==6):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def k (self):
        for r in range (7):
            for c in range (6):
                if (c==0)or(r+c==5 and r!=4)or(r-c==1 and (r!=3 and r!=2)):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def l (self):
        for r in range (7):
            for c in range (6):
                if (c==0)or (r==6):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def m (self): 
        for r in range (7):
            for c in range (6):
                if (c==0 or c==5)or (r==1 and(c==1 or c==4))or (r==2 and(c==2 or c==3)):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def n (self): 
        for r in range (7):
            for c in range (6):
                if (c==0 or c==5)or(c==r):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def o (self): 
        for r in range (7):
            for c in range (6):
                if ((c==0 or c==5)and(r!=0 and r!=6)) or ((r==0 or r==6)and(c!=0 and c!=5)):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def p (self): 
        for r in range (7):
            for c in range (6):
                if (c==0)or((r==0 or r==3)and c!=5)or(c==5 and (r==1 or r==2)):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def q (self): 
        for r in range (7):
            for c in range (6):
                if (c==0 and (r!=0 and r!=6))or (c==5 and (r!=5 and r!=0)) or (r==0 and (c!=0 and c!=5)) or (r==6 and (c!=4 and c!=0))or (r-c==1 and r>3):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def r (self): 
        for r in range (7):
            for c in range (6):
                if (c==0)or((r==0 or r==3)and c!=5) or(c==5 and (r==1 or r==2))or(r-c==1 and r>3):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def s (self): 
        for r in range (7):
            for c in range (6):
                if (r==3)or(c==0 and(r>0 and r<4))or(c==5 and(r>3 and r<6))or((r==0 or r==6)and(c!=0 or c!=5)):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def t (self): 
        for r in range (7):
            for c in range (6):
                if ((r==0)and c!=0)or (c==3):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def u (self): 
        for r in range (7):
            for c in range (6):
                if ((c==0 or c==5)and r!=6) or ((r==6)and(c!=0 and c!=5)):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def v (self): 
        for r in range (7):
            for c in range (6):
                if ((c==0 or c==5)and(r<3))or((c==1 or c==4)and(r>2 and r<6))or(r==6 and (c==2 or c==3)):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def w (self): 
        for r in range (7):
            for c in range (6):
                if (c==0 or c==5)or (r==5 and(c==1 or c==4))or (r==4 and(c==2 or c==3)):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def x (self): 
        for r in range (7):
            for c in range (6):
                if ((r-c==0 or r+c==5) and r<4)or((r+c==6 or r-c==1)and r>2):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def y (self): 
        for r in range (7):
            for c in range (6):
                if ((r-c==0 or r+c==5) and r<3)or(c==3 and r>2)or(r==6 and c==2):
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()
    def z (self): 
        for r in range (7):
            for c in range (6):
                if(r==0 or r==6)or(r+c==5):                
                    print('0',end='')
                else:
                    print(end=' ')
            print()
        print()

a=alphabets()
(a.a())
(a.b())
(a.c())
(a.d())
(a.e())
(a.f())
(a.g())
(a.h())
(a.i())
(a.j())
(a.k())
(a.l())
(a.m())
(a.n())
(a.o())
(a.p())
(a.q())
(a.r())
(a.s())
(a.t())
(a.u())
(a.v())
(a.w())
(a.x())
(a.y())
(a.z())




