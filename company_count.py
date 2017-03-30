from report import *

def show_company_count(S):
    print "Company Count\t\tSubmission Count"
    
    for (company, count) in S.company_count().items():
        if company:
            print "%s\t\t%s" % (company.ljust(20), count)

if __name__ == "__main__":
    show_company_count(S)
