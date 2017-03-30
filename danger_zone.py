from report import *
from show_report import *
import sys

if __name__ == "__main__":
    min_vote = 3.5
    max_vote = 3.8
    min_count = 3
    S = ALL.standard()
    S = S.filter(lambda s: s.average >= min_vote and s.average < max_vote and s.count >= min_count)
    show_report(S, "danger_zone.csv")
    #S.print_subs()
    # if 'O' in sys.argv:
    #     S.open_links()

    # if 'L' in sys.argv:
    #     S.print_links()
