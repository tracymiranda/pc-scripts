from report import *
import sys

if __name__ == "__main__":
    S = Submissions.from_path(path).no_psql().standard()
    if 'C' in sys.argv:
        ids = filter(lambda s: s != 'C', sys.argv[1:-1])
        S = S.filter(lambda s: s in map(lambda id: index[id], ids))
        S.print_subs()
        S.connect(sys.argv[-1])
    else:
        ids = sys.argv[1:]
        S = S.filter(lambda s: s in map(lambda id: index[id], ids))
        S.print_subs()
        

