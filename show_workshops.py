from report import *
from show_report import *
import sys

if __name__ == "__main__":
    S = ALL.tutorials()#.vote_cutoff(3.0)

    # show_report(S, 'tutorials.csv')
    S.print_subs()
