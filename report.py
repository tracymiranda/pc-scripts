import os, csv, sys
from itertools import *
from subprocess import call
import sqlite3

fields = ['Title', 'Session Type', 'Track', 'Body', 'Speaker(s)', 'Status', 'Experience level', 'AVG', 'Vote Count', 'Standard Deviation', 'PC Tags', 'Link' ]
row_index = dict(map(lambda (x, y): (y, x), (enumerate(fields))))

# Community vote
cv_fields = ['Node ID', 'Sessions', '1 star', '2 stars', '3 stars', '4 stars', '5 stars', 'Total']
cv_row_index = dict(map(lambda (x, y): (y, x), (enumerate(cv_fields))))

def connect_subs(subs, label):
    for src in subs:
        for dst in subs:
            if src != dst:
                src.connections.append( (dst, label) )
                dst.connections.append( (src, label) )

class Submissions:
    @classmethod
    def from_paths(cls, submissions_path, cv_path):
        m = { }
        with open(submissions_path, 'rb') as f:
            reader = csv.reader(f)
            for row in list(reader)[1:]:
                entry = { }
                for field in fields:
                    entry[field] = row[row_index[field]]
                m[entry['Title']] = entry

        with open(cv_path, 'rb') as f:
            reader = csv.reader(f)
            for row in list(reader)[1:]:
                entry = { }
                for field in cv_fields:
                    entry[field] = row[cv_row_index[field]]
                # Tie it to the submission
                if not entry['Sessions'] in m:
                    raise Exception("Community vote doesn't match up: %s" % entry['Session'])

                m[entry['Sessions']]['cv_1'] = entry['1 star']
                m[entry['Sessions']]['cv_2'] = entry['2 stars']
                m[entry['Sessions']]['cv_3'] = entry['3 stars']
                m[entry['Sessions']]['cv_4'] = entry['4 stars']
                m[entry['Sessions']]['cv_5'] = entry['5 stars']

        # Join the
        subs = map(lambda x: Submission(x), m.values())
        return Submissions(subs)

    def __init__(self, subs):
        subs = filter(lambda s: not s.isDuplicate, subs)
        self.subs = filter(lambda s: not s.isKeynote, subs)

        self.tags = list(set([tag for s in self.subs for tag in s.tags]))
        self.size = len(self.subs)

#     def tag_count(self):
#         return len(set(tag_count().keys()))

    def new_speakers(self):
        return len(filter(lambda s: s.isNew, self.subs))

    def no_psql(self):
        return Submissions(filter(lambda s: not s.isPsql, self.subs))

    def vote_cutoff(self, min_vote):
        return self.filter(lambda s: s.average >= min_vote)

    def count_cutoff(self, min_count):
        return self.filter(lambda s: s.count >= min_count)
    
    def ignite(self):
        return Submissions(filter(lambda s: s.session in ['Ignite (5 minutes)'], self.subs))   
    
    def showtime_demo(self):
        return Submissions(filter(lambda s: s.session in ['Showtime Demo'], self.subs))           

    def standard(self):
        return Submissions(filter(lambda s: s.session in ['Standard [35 minutes]'], self.subs))

    def vote_count(self):
        counts = []
        for submission in filter_psql(self.subs):
            counts.append(submission.count)

        groups = { }
        for vote in counts:
            if not vote in groups:
                groups[vote] = 0
            groups[vote] += 1
        return groups

    def community_vote_count(self):
        counts = []
        for submission in filter_psql(self.subs):
            counts.append(submission.cv_total)

        groups = { }
        for vote in counts:
            if not vote in groups:
                groups[vote] = 0
            groups[vote] += 1
        return groups

    def tag_count(self):
        tags = []
        for sub in self.subs:
            tags += sub.tags

        groups = { }
        for tag in tags:
            if not tag in groups:
                groups[tag] = 0
            groups[tag] += 1
        return groups

    def project_count(self):
        projects = []
        for sub in self.subs:
            projects += sub.projects

        groups = { }
        for project in projects:
            if not project in groups:
                groups[project] = 0
            groups[project] += 1
        return groups

    def company_count(self):
        companies = []
        for sub in self.subs:
            companies.append(sub.company)

        groups = { }
        for company in companies:
            if not company in groups:
                groups[company] = 0
            groups[company] += 1
        return groups

    def track_count(self):
        companies = []
        for sub in self.subs:
            companies.append(sub.track)

        groups = { }
        for track in companies:
            if not track in groups:
                groups[track] = 0
            groups[track] += 1
        return groups

    def speaker_count(self):
        speakers = []
        for sub in self.subs:
            speakers += sub.speakers

        groups = { }
        for speaker in speakers:
            if not speaker in groups:
                groups[speaker] = 0
            groups[speaker] += 1

        return groups

    def filter(self, predicate):
        return Submissions(filter(predicate, self.subs))

    def find_title(self, title):
        subs = filter(lambda s: s.title == title, self.subs)
        if len(subs) == 0:
            raise Exception("Title '%s' not found" % title)
        if len(subs) != 1:
            raise Exception("Multiple of title %s found" % title)

        return subs[0]

    def find_titles(self, title):
        return self.filter(lambda s: title.lower() in s.title.lower())

    def find_speaker(self, speaker):
        return self.filter(lambda s: any(filter(lambda sp: speaker.lower() in sp.lower(), s.speakers)))

    def find_tag(self, tag):
        return self.filter(lambda s: any(filter(lambda t: tag == t, s.tags)))

    def find_company(self, company):
        return self.filter(lambda s: s.company == company)

    def find_track(self, track):
        return self.filter(lambda s: s.track == track)

    def find_project(self, project):
        return Submissions(filter(lambda s: project in s.projects, self.subs))

    def links(self):
        links = []
        for s in self.subs:
            links.append(s.link)
        return links

    def open_links(self, yes_im_sure = False):
        if(len(self.links()) > 40 and not yes_im_sure):
            print "There are %d links to open...are you sure? If so, pass in True" % (len(self.links()))
        else:
            cmd = """open -a "Google Chrome" %s""" % ' '.join(self.links())
            print "Opening %d links..." % (len(self.links()))
            call(cmd, shell=True)

    def print_subs(self):
        print "Title\t\t\t\t\t\tVote\tVotes\tstd"
        for s in self.subs:
            t = s.title[:40].ljust(45)
            if s.accepted:
                t = '* ' + t
            comvotes = "ComVotes: %d  %d  %d  %d  %d" % (s.cv[0], s.cv[1], s.cv[2], s.cv[3], s.cv[4])
            comvotes = comvotes.ljust(45)
            print "%s\t%.2f\t%d\t%.2f" % (t, s.average, s.count, s.std)
            print "%s\t%.2f\t%d" % (comvotes, s.cv_average, s.cv_total)
            print " Company: %s" % s.company
            print " Project: %s" % ', '.join(s.projects)
            print " Speaker: %s" % ', '.join(s.speakers)
            print "    Link: %s" % s.link
            print "  Is New: %s" % s.isNew
            print "    Tags: %s" % ' '.join(s.tags)
            print "      ID: %s" % s.id
            print
        print "Total: %d" % self.size

    def print_links(self):
        for s in self.subs:
            print s.link

    def union(self, other):
        return Submissions(set(self.subs).union(set(other.subs)))

    def intersect(self, other):
        return Submissions(set(self.subs).intersect(set(other.subs)))

    def diff(self, other):
        return Submissions(set(self.subs).difference(set(other.subs)))

    def edges(self):
        e = []
        considered = set([])
        for s in self.subs:
            for (dst, label) in s.connections:
                l = sorted([s.id, dst.id])
                t = (l[0], l[1])
                if not t in considered:
                    considered.add(t)
                    e.append((s, dst, label))

        return e

    def labels(self):
        ls = { }
        considered = set([])

        for (src, dst, label) in S.edges():
            if not label in ls.keys():
                ls[label] = set([])
            ls[label].add(src)
            ls[label].add(dst)
        return ls

    def find_label(self, label):
        labels = self.labels()
        if label in labels.keys():
            return labels[label]
        else:
            return []

    def save_subs(self, path = "submissions.trunc.csv"):
        line = '"%s", %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
        header = line % ("Title", "ID", "Vote", "Vote_Count", "Comm_Vote", "Comm_Vote_Count", "Speakers", "Company", "Track", "Accepted", "TAG1", "TAG2", "TAG3", "TAG4", "TAG5", "TAG6", "TAG7", "TAG8", "LINK")
        lines = [header]
        for s in self.subs:
            tags = map(lambda x: '', range(0, 8))
            for (i, tag) in enumerate(s.tags):
                tags[i] = tag
            accepted = ''
            if s.accepted:
                accepted = '*'
            lines.append(line % (s.title,
                                 s.id,
                                 str(s.average),
                                 str(s.count),
                                 str(s.cv_average),
                                 str(s.cv_total),
                                 ' '.join(s.speakers),
                                 str(s.company),
                                 s.track, accepted,
                                 tags[0],
                                 tags[1],
                                 tags[2],
                                 tags[3],
                                 tags[4],
                                 tags[5],
                                 tags[6],
                                 tags[7],
                                 s.link))

        txt = '\n'.join(lines)
        with open(path, 'w') as f:
            f.write(txt)
        print "Saved %d submissions to %s" % (self.size, path)

    def mark_accepted(self):
        conn = sqlite3.connect('program.db')
        c = conn.cursor()
        count = 0
        for s in self.subs:
            if not c.execute("SELECT * FROM accepted WHERE id = '%s'" % s.id).fetchone():
#                print "INSERT INTO accepted VALUES('%s')" % s.id
                c.execute("INSERT INTO accepted VALUES('%s')" % s.id)
                count += 1
        conn.commit()
        print "Marked %d (out of %d) as newly accepted" % (count, self.size)

    def connect(self, label):
        edges = set([])
        for s1 in self.subs:
            for s2 in self.subs:
                if s1 != s2:
                    l = sorted([s1.id, s2.id])
                    if l[0] == s1.id:
                        edges.add( (s1, s2) )
                    else:
                        edges.add( (s2, s1) )
        conn = sqlite3.connect('program.db')
        c = conn.cursor()
        for src, dst in edges:
            c.execute("SELECT label FROM edges ORDER BY label DESC")
            id = int(c.fetchone()[0]) + 1
            insert = "INSERT INTO labels VALUES ('%d','%s')" % (id, label)
            print insert
            c.execute("INSERT INTO labels VALUES ('%d','%s')" % (id, label))
            c.execute("INSERT INTO edges VALUES ('%s','%s','%d')" % (src.id, dst.id, id))
        conn.commit()
        print "%d submissioned tied together with label %s" % (self.size, label)



class Submission:
    def __init__(self, fields):
        self.title = fields['Title'].strip()
        self.session = fields['Session Type'].strip()
        self.track = fields['Track'].strip()
        self.body = fields['Body'].strip()
        raw_speakers = fields['Speaker(s)']
        raw_speakers = raw_speakers.replace('),', ')|')
        self.speakers = filter(lambda s: not (']' in s and not '[' in s),
                               map(lambda x: x.strip(), raw_speakers.split('|')))
        self.status = fields['Status'].strip()
        self.level = fields['Experience level'].strip()
        self.average = float(fields['AVG'].split('/')[0].strip())
        self.count = int(fields['Vote Count'])
        self.std = float(fields['Standard Deviation'].strip())
        self.link = fields['Link'].strip()
        self.id = self.link[-4:]

        # Community votes
        self.cv = [0, 0, 0, 0, 0]
        self.cv[0] = int(fields["cv_1"])
        self.cv[1] = int(fields["cv_2"])
        self.cv[2] = int(fields["cv_3"])
        self.cv[3] = int(fields["cv_4"])
        self.cv[4] = int(fields["cv_5"])
        self.cv_total = sum(self.cv)
        self.cv_average = 0
        if self.cv_total > 0:
            self.cv_average = (self.cv[0] + (2.0 * self.cv[1]) + (3.0 * self.cv[2]) + (4.0 * self.cv[3]) + (5.0 * self.cv[4])) / self.cv_total

        # Deal with tags

        tags = filter(lambda tag: tag != "", map(lambda tag: tag.strip(), fields['PC Tags'].split('\n')))
        self.raw_tags = tags

        # Company
        company_tags = filter(lambda tag: tag.startswith("company:"), tags)
        if len(company_tags) > 1:
            raise Exception("There are too many company tags on talk at %s" % (self.link))
        elif len(company_tags) == 1:
            self.company = company_tags[0].split(':')[1].strip()
        else:
            self.company = None

        tags = filter(lambda tag: not tag.startswith("company:"), tags)

        # Project
        project_tags = filter(lambda tag: tag.startswith("project:"), tags)
        self.projects = map(lambda tag: tag.split(':')[1], project_tags)

        tags = filter(lambda tag: not tag.startswith("project:"), tags)

        self.isNew = "newspeaker" in tags or "new" in tags
        tags = filter(lambda tag: tag != "newspeaker", tags)
        tags = filter(lambda tag: tag != "new", tags)

        self.isDuplicate = "duplicate" in tags
        tags = filter(lambda tag: tag != "duplicate", tags)

        self.isKeynote = "keynote" in tags
        tags = filter(lambda tag: tag != "keynote", tags)

        self.isEarlybird = "early-bird" in tags
        tags = filter(lambda tag: tag != "early-bird", tags)

        self.accepted = 'accept' in tags
        tags = filter(lambda tag: tag != "accept", tags)

        self.waitlisted = 'waitlist' in tags
        tags = filter(lambda tag: tag != "waitlist", tags)

        # filter out tags I don't want
        dont_include_tags = ['mapbox', 'pick', 'nov17']
        tags = filter(lambda tag: not tag in dont_include_tags, tags)
        self.tags = tags

        # Figure out some properties

        self.isPsql = self.track == "PostgreSQL Day"
        self.isDeclined = self.status == 'Declined'

        # List of connected subs, tuples (sub, label)
        self.connections = []

        if self.isEarlybird:
            self.accepted = True
            self.average = 5.0

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)

def filter_psql(subs):
    return filter(lambda s: not s.isPsql, subs)

def show_vote_count(S):
    print "Vote Count\t\tSubmission Count"

    for (vote, count) in S.vote_count().items():
        print "%s\t\t%s" % (vote, count)

def group_links(S):
    links = []
    for s in S.subs:
        links.append(s.link)
    chunks = []
    for i in range(0, len(links), 15):
        cmd = """open -a "Google Chrome" %s""" % ' '.join(links[i:i + 15])
        chunks.append(cmd)
    open('links.txt', 'w').write('\n\n'.join(chunks))
    print "Done."

def save_links(S):
    cmd = 'open -a "Google Chrome" %s'
    links = []
    for s in S.subs:
        links.append(s.url)
    chunks = []
    for i in range(0, len(links), 15):
        chunks.append(' '.join(links[i:i + 15]))
    open('links.txt', 'w').write('\n\n'.join(chunks))
    print "Done."

def show_header(S, min_vote = 0):
    print "%d submissions at or above %f average." % (len(S.subs), min_vote)
    print "%d of which are from new speakers." % (S.new_speakers())


submissions_path = 'submissions.csv'
cv_path = 'community-votes.csv'
min_vote = 0
#min_vote = 2.5
#min_vote = 3.5
#min_vote = 4.0
#min_vote = 3.5

ALL = Submissions.from_paths(submissions_path, cv_path).no_psql()
index = { }
for s in ALL.subs:
    index[s.id] = s

def load_db():
    # Fill in edges
    conn = sqlite3.connect('program.db')
    c = conn.cursor()
    for (src, dst, label) in c.execute("SELECT src, dst, description FROM edges JOIN labels ON edges.label == labels.id "):
        src = index[src]
        dst = index[dst]
        src.connections.append( (dst, label) )
        dst.connections.append( (src, label) )

    # for src in c.execute("SELECT * FROM accepted"):
    #     index[src[0]].accepted = True

#load_db()

S = ALL.standard()#.filter(lambda s: s.accepted)

if __name__ == '__main__':
#    min_vote = 3.5
    min_vote = 0.0

    if len(sys.argv) > 1:
        min_vote = float(sys.argv[1])

    S = ALL.standard().filter(lambda s: s.accepted)
    show_header(S, min_vote)

    print "There are %d accepted, %d not accepted." % (len(S.filter(lambda s: s.accepted).subs), len(S.filter(lambda s: not s.accepted).subs))

    if 'O' in sys.argv:
        S.open_links()

    if 'S' in sys.argv:
        S.save_subs()
