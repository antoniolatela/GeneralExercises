#from myprog import MyFunc
import myprog

class One():
    def __init__(self):
        print ("Hi init!")

    def foo(self):
        print ("I'm foo")
        print("bar")

    def listz (self):
        #List
        #print("Test Lists")
        l =  [1,1,1,1,1,1,2,3,4,5]
        l[4] = 'hi there!'
        l.append(1974)
        #print (l[-2], l[-1])
        l.append(l)
        #l[1] = 123
        return l[-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1]

    def getRangeCount(self):
        for i in range (0, len(self.listz())):
            print (i,self.listz()[i])

    def getSlice(self, a=0, b=None):
        print(self.listz()[a:b])

    def strings (self, s='alpha'):
        print(s[0])
        #s[1]='abc' Errorù

    def tuple(self):
        t = {1,2,3,4,5}

    def callExtMod(self):
        myprog.MyFunc()

        #MyFunc()
#One().foo()
#One().listz()




one = One()
one = One()
one.tuple()
one.callExtMod()
#one.getRangeCount()
