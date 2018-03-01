import problem
import ride


def getLibreVehicle(vlis):
    for v in len(vlis):
        if v.r < 0:
            return v
    return -1

def getRide():
    contp += 1
    return p.rideList[contp]


def assign():
    v = getLibreVehicle()
    while v > -1:
        ride = getRide()
        v.r = ride.id
        v=getLibreVehicle()




class solution():
    def __init__(self,F):
        for element in range(F):
            self.vehicles.append([])




class vehicle():
    def __init__(self,x=0,y=0,rideID=-1):
        self.x = x
        self.y = y
        self.r = rideID

p = problem(2,4,2,3,2,10)
p.rideList = [ride(0,0, 0, 1, 3, 2, 9), ride(1,1, 2, 1, 0, 0, 9), ride(2,2, 0, 2, 2, 0, 9)]
contp = -1

p.rideList.sort()
vlis = []
for element in range(p.F):
    vlis.append(vehicle)

for t in range(p.T):
    assign()
    avance()


