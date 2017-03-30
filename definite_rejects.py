from report import *
from show_report import *
import sys

if __name__ == "__main__":
    max_vote = 3.2
    min_count = 3
    S = ALL.standard()
    S = S.filter(lambda s: s.average < max_vote and s.count >= min_count)
    show_report(S, "definite_rejects.csv")
    #S.print_subs()
    # if 'O' in sys.argv:
    #     S.open_links()

    # if 'L' in sys.argv:
    #     S.print_links()
