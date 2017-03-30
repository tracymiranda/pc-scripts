from report import *
import sys

def process_tutorials(S, min_vote, open_tabs):
    S = S.tutorials()
    
    S = S.vote_cutoff(min_vote)
    show_header(S)
    print
    show_vote_count(S)
    show_tag_count(S)
    if open_tabs:
        S.open_links()

if __name__ == "__main__":
    min_vote = 3.0

    process_tutorials(S, min_vote, 'O' in sys.argv)
