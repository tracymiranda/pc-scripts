from report import *
import sys

if __name__ == '__main__':
    SL = ALL.tutorials().filter(lambda s: s.accepted)
    SR = ALL.tutorials().filter(lambda s: 'accept' in s.raw_tags)

    need_tags = SL.diff(SR)
    print "Need Tags:"
    need_tags.print_subs()
    print

    if 'O!' in sys.argv:
        need_tags.open_links(True)
    elif 'O' in sys.argv:
        need_tags.open_links()


    wrong_tags = SR.diff(SL)
    print "Wrong Tags:"
    wrong_tags.print_subs()
