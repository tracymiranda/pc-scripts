from report import *
from show_report import *
import sys, math

if __name__ == "__main__":
    contention_threshold = float(sys.argv[1])

    S = ALL#.standard()
    S = S.filter(lambda s: abs(s.cv_average - s.average) > contention_threshold)
    #show_report(S, "query.csv")
    S.print_subs()
