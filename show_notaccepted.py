from report import *
from show_report import *
import sys

if __name__ == "__main__":
    S = ALL.standard().vote_cutoff(3.0)
    S = S.filter(lambda s: not s.accepted)

    show_report(S, 'notaccepted.csv')
