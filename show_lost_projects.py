from report import *
from show_report import *
import sys

if __name__ == "__main__":
    min_vote = float(sys.argv[1])
    S = ALL.standard()
    Sbelow = S.filter(lambda s: s.average < min_vote)
    Sabove = S.filter(lambda s: s.average >= min_vote)
    Pbelow = set(Sbelow.project_count().keys())
    Pabove = set(Sabove.project_count().keys())
    lost = Pbelow - Pabove

    for project in lost:
        if project:
            print "%s" % project
