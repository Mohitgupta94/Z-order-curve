print "Enter 2 numbers separated by single space"
def getZOrder(a):
    i=0
    b=0
    while(a!=0):
        R=a%2
        a=a/2
        b=b+((4**i)*R)
        i=i+1
    return b
e=raw_input()
x=int(e[0])
y=int(e[2])
m=getZOrder(x)
n=2*getZOrder(y)
print m+n