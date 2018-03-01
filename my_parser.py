import problem
import ride
import re


def run(file):
    file_ = open(file)

    first_line = file_.readline()
    tmp = re.split(" ", first_line)
    p = problem.problem(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5])

    line = file_.readline()
    while line:
        tmp = re.split(" ", line)
        r = ride.ride(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5])
        p.append_ride(r)
        line = file_.readline()

    return p


