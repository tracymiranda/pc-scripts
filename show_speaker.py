from report import *
import sys

if __name__ == '__main__':
    speaker = sys.argv[1]
    S = S.find_speaker(speaker)
    S.print_subs()

    if 'O' in sys.argv:
        S.open_links()

