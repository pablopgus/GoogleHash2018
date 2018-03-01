import my_parser
import problem
import ride


my_parser.run('a_example.in')

def getLibreVehicle(vlis):
    for v in len(vlis):
        if v.r < 0:
            return v;
    return -1


class


class vehicle():
    def __init__(self,x=0,y=0,rideID=-1):
        self.x = x
        self.y = y
        self.r = rideID

p = problem(2,4,2,3,2,10)
p.rideList = [ride(0,0, 0, 1, 3, 2, 9), ride(1,1, 2, 1, 0, 0, 9), ride(2,2, 0, 2, 2, 0, 9)]

p.rideList.sort()
vlis = []
for element in range(p.F):
    vlis.append(vehicle)
contp = 0
#for t in range(p.T):
