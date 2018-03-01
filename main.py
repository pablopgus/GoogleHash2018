import my_parser
import problem
import ride

def getLibreVehicle(vlis):
    for v in len(vlis):
        if v.r < 0:
            return v
    return -1

class vehicle():
    def __init__(self,x=0,y=0,rideID=-1):
        self.x = x
        self.y = y
        self.r = rideID


# Acquire the problem.
p = my_parser.run('a_example.in')
p.rideList.sort()

for elem in p.rideList:
    print(elem.id)
