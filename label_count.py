from report import *

def show_label_count(S):
    print "Label\t\tSubmission Count"

    labels = S.labels()

    for (label, subs) in labels.items():
        print "%s\t\t%s" % (label, len(subs))

if __name__ == "__main__":
    show_label_count(S)
