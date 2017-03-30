from report import *
import sys

def show_report(S, save_path = '', min_vote=0.0):
    #S.print_subs()
    show_header(S, min_vote)

    print "Companies:"
    for (company, count) in sorted(S.company_count().items(), key=lambda (c, _): c):
        if company:
            print "  %s\t\t%s" % (company.ljust(20), count)

    print "Tracks:"
    for (track, count) in S.track_count().items():
        if track:
            print "  %s\t\t%s" % (track.ljust(20), count)

    print "Speakers with more than one talk"
    for (speaker, count) in S.speaker_count().items():
        if count > 1:
            print "  %s\t\t%s" % (speaker.ljust(48), count)

    if 'O!' in sys.argv:
        S.open_links(True)
    elif 'O' in sys.argv:
        S.open_links()


    if 'L' in sys.argv:
        S.print_links()

    if 'S' in sys.argv:
        S.save_subs(save_path)

    # if 'A' in sys.argv:
    #     S.mark_accepted()
