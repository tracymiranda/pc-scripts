from report import *
import sys
from subprocess import call

path = "FOSS4G NA 2015 Program - Rough Draft - Sheet6.csv"

subs = []
with open(path, 'rb') as f:
    reader = csv.reader(f)
    for row in list(reader)[1:]:
        day = row[0]
        time = row[1].replace("-", "to")
        room8_talk = S.find_title(row[2])
        room9_talk = S.find_title(row[3])
        room10_talk = S.find_title(row[4])

        room8_talk.time = "Room 8 - %s - %s" % (day, time)
        room9_talk.time = "Room 9 - %s - %s" % (day, time)
        room10_talk.time = "Room 10 - %s - %s" % (day, time)
        subs += [room8_talk, room9_talk, room10_talk]

for s in subs:
    print
    print s.title
    print s.time
    raw_input("Press Enter to open...")
    print s.title
    print s.time
    cmd = """open -a "Google Chrome" %s/edit""" % s.link
    call(cmd, shell=True) 

