from report import *
import sys

if __name__ == "__main__":
    projects = sys.argv[1:]
    minvote_args = filter(lambda x: x.startswith("minvote:"), projects)
    min_vote = map(lambda x: float(x.split(':')[1]), minvote_args)
    if len(min_vote) > 0:
        min_vote = min_vote[0]
    else:
        min_vote = 0.0

    projects = filter(lambda x: not x.startswith("minvote:"), projects)

    merged = Submissions([])
    for project in projects:
        merged = merged.union(S.find_project(project))

    S = merged.filter(lambda s: s.average >= min_vote)
    S.print_subs()

    if 'O' in sys.argv:
        S.open_links()
