from report import *
import sys

if __name__ == "__main__":
    language = sys.argv[1]
    S = S.find_language(language)

    S.print_subs()

    if 'O' in sys.argv:
        S.open_links()
