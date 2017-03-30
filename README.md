# pc-scripts
Handy scripts used by the program committee for processing talk proposals.

This version is adapted for processing proposals for EclipseCon France 2017

Pre-requisites
---------------
* Python 2.7(or higher) installed and runnable from the path

To Run
--------------
CSV data can be downloaded manually from the Conference website `Administer Sessions` page (login required)
1. https://www.eclipsecon.org/france2017/pc-admin/sessions/eclipsecon-admin-unprocessed.csv (download as submissions.csv)
2. https://www.eclipsecon.org/france2017/community-voting/report.csv (download as community-votes.csv)
Or alternatively you can modify `dl.py` and save off your PC credentials locally. 

`report.py` is the main "library" behind the other scripts.
There are lots of scripts that do things manually, for FOSS4G by the end mainly running `qs.py` was providing the main information, based on particular pc tags.
