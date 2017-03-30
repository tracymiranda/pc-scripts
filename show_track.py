from report import *
import sys

if __name__ == "__main__":
    tracks = filter(lambda x: x != 'O', sys.argv)
    merged = Submissions([])
    for track in tracks:
        merged = merged.union(S.find_track(track))

    S = merged

    S.print_subs()

    if 'O' in sys.argv:
        S.open_links()
