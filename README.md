# pc-scripts
Handy scripts used by the program committee for processing talk proposals.

This version is adapted for processing proposals for EclipseCon France 2017

Pre-requisites
---------------
* Python 2.7 installed and runnable from the path

To Run
--------------
The scripts require two CSV files locally to run. CSV data can be downloaded manually from the Conference website `Administer Sessions` page (login required)
* https://www.eclipsecon.org/france2017/pc-admin/sessions/eclipsecon-admin-unprocessed.csv (download as submissions.csv)
* https://www.eclipsecon.org/france2017/community-voting/report.csv (download as community-votes.csv)
Or alternatively you can modify `dl.py` and save off your PC credentials locally. 

`report.py` is the main "library" behind the other scripts. There are lots of individual scripts for now, e.g.
* `show_track.py` shows the number of submitted talks per track
* `speaker_count.py` shows speakers with >1 talk 

`qs.py` will be updated in due course to be the master script. 