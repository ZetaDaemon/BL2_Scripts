from dataclasses import replace
import re, sys

BASEOBJ = "BASEOBJ"
TRUEMAXSTACKS = "TRUEMAXSTACKS"
FAKEMAXSTACKS = "FAKEMAXSTACKS"
SKILLEVENT = "SKILLEVENT"
SKILLDURATION = "SKILLDURATION"
SKILLHUDSLOT = "SKILLHUDSLOT"
TRACKEDICON = "TRACKEDICON"


def main(argv):
    if len(argv) != 7:
        print("skillgen.py <BASEOBJ> <TRUEMAXSTACKS> <FAKEMAXSTACKS> <SKILLEVENT> <SKILLDURATION> <SKILLHUDSLOT> <TRACKEDICON>")
        sys.exit()
    input = open("blueprint.txt", "r")
    output = open("out.txt", "w")
    for l in input:
        l = re.sub(BASEOBJ, argv[0], l)
        l = re.sub(TRUEMAXSTACKS, argv[1], l)
        l = re.sub(FAKEMAXSTACKS, argv[2], l)
        l = re.sub(SKILLEVENT, argv[3], l)
        l = re.sub(SKILLDURATION, argv[4], l)
        l = re.sub(SKILLHUDSLOT, argv[5], l)
        l = re.sub(TRACKEDICON, argv[6], l)
        output.write(l)


if __name__ == "__main__":
   main(sys.argv[1:])