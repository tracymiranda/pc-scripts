from report import *
import sys

if __name__ == "__main__":
    company = sys.argv[1]
    S = S.find_company(company)

    S.print_subs()

    if 'O' in sys.argv:
        S.open_links()
