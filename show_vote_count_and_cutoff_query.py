from report import *
from show_report import *
import sys

if __name__ == "__main__":
    min_vote = float(sys.argv[1])
    min_count = int(sys.argv[2])
    S = ALL.standard()
    S = S.filter(lambda s: s.average >= min_vote and s.count >= min_count)
    show_report(S, "query.csv")
    #S.print_subs()
    # if 'O' in sys.argv:
    #     S.open_links()

    # if 'L' in sys.argv:
    #     S.print_links()
