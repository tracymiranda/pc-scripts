from report import *

def show_track_count(S):
    print "Track Count\t\tSubmission Count"
    
    for (track, count) in S.track_count().items():
        if track:
            print "%s\t\t%s" % (track.ljust(20), count)

if __name__ == "__main__":
#    S = ALL.standard().vote_cutoff(4.0)
    S = ALL.standard().filter(lambda s: s.accepted)
    show_track_count(S)
