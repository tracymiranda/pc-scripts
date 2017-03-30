from operator import itemgetter
from report import *

def show_speaker_count(S):
    print "Speaker Count".ljust(40) + "\t\tSubmission Count"

    items = S.speaker_count().items()    
    for (speaker, count) in sorted(items, key=itemgetter(1), reverse=True):
        if count > 1:
            print "%s\t\t%s" % (speaker.ljust(40), count)

if __name__ == "__main__":
    show_speaker_count(S)
