import sys
from report import *

if __name__ == '__main__':

    min_vote = float(sys.argv[1])
    S = ALL.vote_cutoff(min_vote).standard()#.count_cutoff(5)
    show_header(S, min_vote)

    if 'O' in sys.argv:
        S.open_links()
