from report import *

def show_vote_count(S):
    print "Vote Count\t\tSubmission Count"

    for (vote, count) in S.vote_count().items():
        print "%s\t\t%s" % (vote, count)

    print "\nCommunity votes:"

    for (vote, count) in S.community_vote_count().items():
        print "%s\t\t%s" % (vote, count)

if __name__ == "__main__":
    show_vote_count(ALL)
