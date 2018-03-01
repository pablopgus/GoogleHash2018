import ride

class problem():
    def __init__(self, R, C, F, N, B, T):
        self.R = R
        self.C = C
        self.F = F
        self.N = N
        self.B = B
        self.T = T
        self.rideList  = []

    def append_ride(self,r):
        self.rideList.append(r)


