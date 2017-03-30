from report import *

def show_ignite_count(S):
    print "Ignite Talks Count".ljust(40) + "\t\tSubmission Count"
    
    items = S.track_count().items()
    total = sum([count for (track, count) in items])
    for (track, count) in sorted(items, cmp=lambda (a_track, a_count), (b_track, b_count): cmp(b_count, a_count)):
        if track:
            print "%s\t\t%s" % (track.ljust(40), count)
    print "Total".ljust(40) + "\t\t%s" % total

if __name__ == "__main__":
#    S = ALL.standard().vote_cutoff(4.0)
    S = ALL.ignite()#.filter(lambda s: s.accepted)
    show_ignite_count(S)
