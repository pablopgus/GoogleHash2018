import my_parser
import problem
import ride

class vehicle():
    def __init__(self,x=0,y=0,rideID=-1):
        self.x = x
        self.y = y
        self.r = rideID

class Solution():
    def __init__(self,F):
        self.vehicles = []
        self.rideSols = []
        i = 0
        for element in range(F):
            self.vehicles.append(vehicle(0,0))
            i = i + 1
            self.rideSols.append([])


    def getLibreVehicle(self):
        for v in self.vehicles:
            if v.r < 0:
                return v
        return -1

    def getRide(self):
        contp += 1
        return p.rideList[contp]


    def assign(self):
        v = self.getLibreVehicle()
        while v.r > -1:
            ride = self.getRide()
            v.r = ride.id
            v=self.getLibreVehicle()

    def avance(self):
        # Asignar las rutas a las litas.
        
        pass








# Acquire the problem.
p = my_parser.run('a_example.in')
p.rideList.sort()
contp = -1

# Iniciar la lista.
vlis = []
for element in range(p.F):
    vlis.append(vehicle)

# Solution finder.
S = Solution(p.F);
for t in range(p.T):
    S.assign()    # Selección de vehiculo.
    S.avance()


