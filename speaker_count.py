from report import *

def show_speaker_count(S):
    print "Speaker Count\t\tSubmission Count"
    
    for (speaker, count) in S.speaker_count().items():
        if count > 1:
            print "%s\t\t%s" % (speaker.ljust(20), count)

if __name__ == "__main__":
    show_speaker_count(S)
