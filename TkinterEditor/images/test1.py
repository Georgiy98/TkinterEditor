import math

def cos(deg):
    return math.cos(deg/180*math.pi)
def sin(deg):
    return math.sin(deg/180*math.pi)
def getParam(u,i,f,um):
    p=u*i*cos(f)
    z=u/i
    r=z*cos(f)
    x=z*sin(f)
    xm=um/i
    print("P = "+str(u)+"*"+str(i)+"*cos "+str(f)+" = "+str(p))
    print("R = "+str(z)+"*cos "+str(f)+" = "+str(r))
    print("X = "+str(z)+"*sin "+str(f)+" = "+str(x))
    print("Z = "+str(u)+"/"+str(i)+" = "+str(z))
    print("Xm= "+str(um)+"/"+str(i)+" = "+str(xm))

arr=[(21,0.134,12.1,4.9),(21,0.134,58.3,5),
     (10.24,0.06,24.2,0),(11.62,0.06,58.9,0),(22,0.06,41.5,0),
     (10.5,0.08,42,0),(12.2,0.08,42,0),(21.2,0.08,18,0),
     (15,0.074,18.6,0),(15,0.088,-63.2,0),(15.0,0.15,39.3,0),
     (15,0.102,1.6,0),(15,0.092,37.2,0),(15,0.182,17,0)]
for i in arr:
    getParam(i[0],i[1],i[2],i[3])
    print("\n")
