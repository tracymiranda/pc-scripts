from operator import itemgetter

from report import *


def show_track_count(S):
    print "Standard Track Count".ljust(40) + "\t\tSubmission Count"
    
    items = S.track_count().items()
    total = sum([count for (track, count) in items])
    for (track, count) in sorted(items, key=itemgetter(1), reverse=True):
        if track:
            print "%s\t\t%s" % (track.ljust(40), count)
    print "Total".ljust(40) + "\t\t%s" % total

if __name__ == "__main__":
#    S = ALL.standard().vote_cutoff(4.0)
    S = ALL.standard()#.filter(lambda s: s.accepted)
    show_track_count(S)
