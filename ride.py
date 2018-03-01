class ride():
    def __init__(self,sid, a, b, x, y, s, f):
        self.id = sid
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f

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