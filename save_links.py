from report import *

if __name__ == "__main__":
    links = []
    for s in ALL.standard().subs:
        links.append(s.link)
    chunks = []
    for i in range(0, len(links), 15):
        cmd = """open -a "Google Chrome" %s""" % ' '.join(links[i:i + 15])
        chunks.append(cmd)
    open('links.txt', 'w').write('\n\n'.join(chunks))
    print "Done."    

