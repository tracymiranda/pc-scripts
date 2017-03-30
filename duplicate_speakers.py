from report import *

if __name__ == '__main__':
    s2t = { }
    subs = S.subs
    for s in subs:
        for sp in s.speakers:
            if not sp in s2t:
                s2t[sp] = []
            s2t[sp].append(s)

    speaker_count = { }
    for sp, sessions in s2t.items():
        l = len(sessions)
        if l > 1:
            speaker_count[sp] = len(sessions)
            Submissions(sessions).print_subs()
        
    print "Speaker\t\t\tCount"
    for sp, count in speaker_count.items():
        print "%s\t\t%d" % (sp, count)


                
        
