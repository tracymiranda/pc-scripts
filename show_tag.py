from report import *
import sys

if __name__ == "__main__":
    tags = filter(lambda x: x != 'O', sys.argv)

    minvote_args = filter(lambda x: x.startswith("minvote:"), tags)
    min_vote = map(lambda x: float(x.split(':')[1]), minvote_args)
    if len(min_vote) > 0:
        min_vote = min_vote[0]
    else:
        min_vote = 0.0

    tags = filter(lambda x: not x.startswith("minvote:"), tags)

    merged = Submissions([])
    for tag in tags:
        merged = merged.union(S.find_tag(tag))

    S = merged.filter(lambda s: s.average >= min_vote)

    S.print_subs()

    if 'O' in sys.argv:
        S.open_links()
