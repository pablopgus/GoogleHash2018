import math
from math import sqrt
class problem():
    def __init__(self, R, C, F, N, B, T):
        self.R = R
        self.C = C
        self.F = F
        self.N = N
        self.B = B
        self.T = T

        self.rideList  = []

class ride():
    def __init__(self,sid, a, b, x, y, s, f):
        self.id = sid
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f
        self.d = abs(a-x) + abs(b-y)

    def __eq__(self, other):
        return (self.f, self.s) == (other.f, other.s)

    def __ne__(self, other):
        return (self.f, self.s) != (other.f, other.s)

    def __lt__(self, other):
        return (self.f, -self.s) < (other.f, -other.s)

    def __le__(self, other):
        return (self.f, -self.s) <= (other.f, -other.s)

    def __gt__(self, other):
        return (self.f, -self.s) > (other.f, -other.s)

    def __ge__(self, other):
        return (self.f, -self.s) >= (other.f, -other.s)

    def __repr__(self):
        return "%s %s" % (self.f, self.s)

class vehicle():
    def __init__(self,x=0,y=0,rideID=-1):
        self.x = x
        self.y = y
        self.r = rideID

def distanceVR(vehicle, ride):
    return abs(vehicle.x-ride.a) + abs(vehicle.y - ride.b)

p = problem(2,4,2,3,2,10)
p.rideList = [ride(0, 0, 0, 1, 3, 2, 9), ride(1, 1, 2, 1, 0, 0, 9), ride(2, 2, 0, 2, 2, 0, 9)]


vlis = []
for element in range(p.F):
    vlis.append(vehicle())

for element in range(p.N):
    dvp = distanceVR(vlis[0],p.rideList[element])
    if p.rideList[element].s == dvp + 

