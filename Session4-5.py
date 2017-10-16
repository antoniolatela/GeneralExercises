

class One():
    def __init__(self):
        print ("Hi!")

    def foo(self):
        print ("I'm foo")
        print("bar")

    def listz (self):
        #List
        print("Test Lists")
        l =  [1,2,3,4,5]
        l[4] = 'hi there!'
        l.append(1974)
        print (l[-2], l[-1])
        l.append(l)
        l[1] = 123
        print (l[1], l[6][6][6][1])
        return l

    def getRangeCount(self):
        for i in range (0, len(self.listz())):
            print (i,self.listz()[i])

#One().foo()
#One().listz()

one = One()
one.getRangeCount()
