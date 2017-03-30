from report import *
import sys

def show_tag_count(S, min_count):
    dont_care = ['nov17']

    print "Tag\t\tSubmission Count"
    tag_count = S.tag_count()
    for tag in sorted(tag_count.keys()):
        if not tag in dont_care:
            if tag_count[tag] >= min_count:
                print "%s\t\t%s" % (tag.ljust(10), tag_count[tag])

if __name__ == "__main__":
    args = sys.argv

    min_vote = 0.0
    min_count = 0
    if len(args) > 1:
        min_count = int(args[1])

    S = S.vote_cutoff(min_vote)
    show_tag_count(S, min_count)
