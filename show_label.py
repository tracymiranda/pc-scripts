from report import *
import sys

def show_label_count(S):
    print "Label\t\tSubmission Count"

    labels = { }
    considered = set([])

    for (src, dst, label) in S.edges():
        if not label in labels.keys():
            labels[label] = set([])
        labels[label].add(src)
        labels[label].add(dst)

    return labels

if __name__ == "__main__":
    labels = filter(lambda x: x != 'O', sys.argv)
    merged = set([])
    for label in labels:
        merged = merged.union(set(S.find_label(label)))

    S = Submissions(merged)

    S.print_subs()

    if 'O' in sys.argv:
        S.open_links()
