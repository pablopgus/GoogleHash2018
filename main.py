import my_parser
import problem
import ride

class vehicle():
    def __init__(self,x=0,y=0,id=0,rideID=-1):
        self.x = x
        self.y = y
        self.id = id
        self.r = rideID
        self.dx = 0
        self.dy = 0

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

    def getRide(self,v):
        ride = None
        points = -1
        i = 0
        while(i < 20 and i < len(self.P.rideList)):
            r = self.P.rideList[i]
            alpha = 20
            beta = 1
            p = 0
            dvp = self.distanceVR(v,r)

            #if( (self.current_step + r.d + dvp) <= r.f):
            #    p = alpha*r.d;

            #if( ( (self.current_step + dvp) - r.s ) < 2):
            #    p = p + beta*self.P.B

            if( p > points ):
                ride = self.P.rideList.pop(i);
            i += 1

        return ride



    def step(self):
        v_list = self.getLibreVehicle()
        # Asignar rides a vehiculos.
        if len(v_list) > 0:
            for v in v_list:
                if(len(self.P.rideList) > 0):
                    #ride = self.getRide(v)
                    ride = self.P.rideList.pop(0)
                    if(ride is not None):
                        v.r = ride.id
                        v.dx = ride.x
                        v.dy = ride.y
                        self.rideSols[v.id].append(ride.id)
                    else:
                        # ACABA.
                        pass

        for v in self.vehicles:
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

p1.rideList.sort()
p2.rideList.sort()
p3.rideList.sort()
p4.rideList.sort()
p5.rideList.sort()

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
