from report import *

def show_project_count(S):
    print "Project Count\t\tSubmission Count"
    
    for (project, count) in S.project_count().items():
        if project:
            print "%s\t\t%s" % (project.ljust(20), count)

if __name__ == "__main__":
    show_project_count(S)
