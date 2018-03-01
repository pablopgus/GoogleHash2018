import problem
import ride
import re


def run(file):
    file_ = open(file)

    first_line = file_.readline()
    print(first_line)

    line = file_.readline()
    while line:
        tmp = re.split(" ", line)
        print(tmp)
        line = file_.readline()

    prob = []
    return prob


