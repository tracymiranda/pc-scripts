from report import *
import sys

if __name__ == "__main__":
    S = Submissions.from_path(path).no_psql().standard().vote_cutoff(3.0)
    line = '"%s", %s, %s, %s, %s, %s, %s, %s'
    header = line % ("Title", "URL", "Jody", "Beth", "Regina", "Kate", "Andy", "Rob")
    lines = [header]
    for s in S.subs:
        lines.append(line % (s.title, s.link, "", "", "", "", "", ""))

    txt = '\n'.join(lines)
    with open("attendance.csv", 'w') as f:
        f.write(txt)
    print "Done."
