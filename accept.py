from report import *
import sys

if __name__ == "__main__":
    S = ALL.standard()
    S = S.filter(lambda s: s.id in sys.argv[1:])
    S.print_subs()

    if 'A' in sys.argv:
        S.mark_accepted()
