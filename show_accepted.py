from report import *
from show_report import *
import sys

if __name__ == "__main__":
#    S = ALL.tutorials()
    S = ALL.standard()
    S = S.filter(lambda s: s.accepted)

    show_report(S, 'accepted.csv')
