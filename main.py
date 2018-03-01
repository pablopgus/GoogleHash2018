import my_parser
import problem
import ride
import copy

class vehicle():
    def __init__(self,x=0,y=0,id=0,rideID=-1):
        self.x = x
        self.y = y
        self.id = id
        self.r = rideID
        self.ax = 0
        self.by = 0
        self.dx = 0
        self.dy = 0
        self.status = 0

class Solution():
    def __init__(self,P,f):
        self.vehicles = []
        self.rideSols = []
        self.contp = -1
        self.P = P
        self.file = f
        i = 0
        for element in range(self.P.F):
            self.vehicles.append(vehicle(0,0,i))
            i = i + 1
            self.rideSols.append([])

    def distanceVR(self,veh, ride):
        return abs(veh.x - ride.a) + abs(veh.y - ride.b)

    def getLibreVehicle(self):
        res = []
        for v in self.vehicles:
            if v.r < 0:
                res.append(v)
        return res

    def getRide(self, v):
        ride = None
        points = -10000000000000000000000000
        sid = -1
        i = 0
        while (i<50 and i < len(self.P.rideList)):
            r = self.P.rideList[i]
            j = i

            p = -10000000000000000000000000

            while(j < 50 and j < len(self.P.rideList)):
                temp = self.P.rideList[j]
                d = abs(temp.a - r.x) + abs(temp.b - r.y)
                if( d < 10 ):
                    p += 10000000000000000000000000000000
                j += 1


            alpha = 1
            beta = 1
            gamma = 1
            epsilon = 1


            dvp = self.distanceVR(v, r)
            p -= gamma*dvp

            if ((self.current_step + r.d + dvp) <= r.f):
                p = alpha*r.d;

            if (((self.current_step + dvp) - r.s) < 2):
                p = p + beta*self.P.B

            if (p > points):
                sid = i
            i += 1
        ride = self.P.rideList.pop(sid)
        return ride

    def step(self):
        v_list = self.getLibreVehicle()
        # Asignar rides a vehiculos.
        if len(v_list) > 0:
            for v in v_list:
                if(len(self.P.rideList) > 0):
                    ride = self.getRide(v)
                    if(ride is not None):
                        v.r = ride.id
                        v.dx = ride.x
                        v.dy = ride.y
                        v.ax = ride.a
                        v.by = ride.b
                        v.status = 1
                        self.rideSols[v.id].append(ride.id)
                    else:
                        pass

        for v in self.vehicles:
            if(v.status == 1):
                if (v.x < v.ax):
                    v.x += 1
                elif (v.x > v.ax):
                    v.x -= 1
                elif (v.y < v.by):
                    v.y += 1
                elif (v.y > v.by):
                    v.y -= 1
                else:
                    v.status = 2
            elif(v.status == 2):
                if( v.x < v.dx ):
                    v.x += 1
                elif( v.x > v.dx ):
                    v.x -= 1
                elif( v.y < v.dy ):
                    v.y += 1
                elif( v.y > v.dy ):
                    v.y -= 1
                else:
                    v.r = -1
                    v.status = 0

    def solve(self):
        self.current_step = 0
        for t in range(self.P.T):
            self.step()  # Selección de vehiculo.
            self.current_step += 1

        # Print solution.
        f = open(self.file, 'w')
        for rides in self.rideSols:
            line = str(len(rides))
            for r in rides:
                line += ' '
                line += str(r)
            line += '\n'
            f.write(line)

        f.close()







# Acquire the problem.
p1 = my_parser.run('a_example.in')
p2 = my_parser.run('b_should_be_easy.in')
p3 = my_parser.run('c_no_hurry.in')
p4 = my_parser.run('d_metropolis.in')
p5 = my_parser.run('e_high_bonus.in')

p1.rideList.sort(reverse=True)
p2.rideList.sort(reverse=True)
p3.rideList.sort(reverse=True)
p4.rideList.sort(reverse=True)
p5.rideList.sort(reverse=True)

# Solution finder.
S1 = Solution(p1,'a.out');
S2 = Solution(p2,'b.out');
S3 = Solution(p3,'c.out');
S4 = Solution(p4,'d.out');
S5 = Solution(p5,'e.out');


S1.solve()
print("A finished.")
S2.solve()
print("B finished.")
S3.solve()
print("C finished.")
S4.solve()
print("D finished.")
S5.solve()
print("E finished.")
