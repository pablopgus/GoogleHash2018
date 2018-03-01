import problem
import ride
import re


def run(file):
    file_ = open(file)

    first_line = file_.readline()
    tmp = re.split(" ", first_line)
    p = problem.problem(int(tmp[0]), int(tmp[1]), int(tmp[2]), int(tmp[3]), int(tmp[4]), int(tmp[5]) )

    line = file_.readline()
    i = 0
    while line:
        tmp = re.split(" ", line)
        r = ride.ride(i, int(tmp[0]), int(tmp[1]), int(tmp[2]), int(tmp[3]), int(tmp[4]), int(tmp[5]) )
        p.append_ride(r)
        line = file_.readline()
        i = i + 1
    return p


