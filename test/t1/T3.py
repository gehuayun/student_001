
# cs=[i for i in range(5)]
#
# print(cs)
# cf =[(x*y) for x in range(1,10) for y in range(1,10)]

shu=[]

def test_cs():
    for x in range(1,10):
        for y in range(1,x+1):
            if x<y:
                print(x ,"*", y,"=",x*y,end="")
            else:
                print(x,"*",y,"=",x*y)






test_cs()