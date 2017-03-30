from report import *
from show_report import *
import sys, math

if __name__ == "__main__":
    community_vote_count = int(sys.argv[1])

    S = ALL#.standard()
    S = S.filter(lambda s: s.cv_total >= community_vote_count)
    #show_report(S, "query.csv")
    S.print_subs()
