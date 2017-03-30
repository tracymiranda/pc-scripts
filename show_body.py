from report import *
import sys

if __name__ == "__main__":
    S = ALL.standard().filter(lambda s: s.accepted)
    for search in filter(lambda x: x != 'O', sys.argv[1:]):
        S = S.filter(lambda s: search in s.body.lower() or search in s.title.lower())
    S.print_subs()
    if 'O' in sys.argv:
        S.open_links()
