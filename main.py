import my_parser
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

# Acquire the problem.
p = my_parser.run('a_example.in')
p.rideList.sort()
contp = -1

# Solution.

vlis = []
for element in range(p.F):
    vlis.append(vehicle)

for t in range(p.T):
    assign()
    avance()


