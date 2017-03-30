from report import *

def show_language_count(S):
    print "Language Count\t\tSubmission Count"
    
    for (language, count) in S.language_count().items():
        if language:
            print "%s\t\t%s" % (language.ljust(20), count)

if __name__ == "__main__":
    show_language_count(S)
