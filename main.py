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


    def getLibreVehicle(self):
        res = []
        for v in self.vehicles:
            if v.r < 0:
                res.append(v)
        return res

    def step(self):
        v_list = self.getLibreVehicle()
        # Asignar rides a vehiculos.
        if len(v_list) > 0:
            for v in v_list:
                if(len(self.P.rideList) > 0):
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
        for t in range(self.P.T):
            self.step()  # Selección de vehiculo.

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
