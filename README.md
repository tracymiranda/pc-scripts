# pc-scripts
Handy scripts used by the program committee for processing talk proposals.

This version is adapted for processing proposals for EclipseCon France 2017

Pre-requisites
---------------
* Python 3.6.0(or higher) installed and runnable from the path

To Run
--------------
CSV data can be downloaded manually from the Conference website `Administer Sessions` page.
Or alternatively you can modify `dl.py` and save off your PC credentials locally. 

`report.py` is the main "library" behind the other scripts.
There are lots of scripts that do things manually, for FOSS4G by the end mainly running `qs.py` was providing the main information, based on particular pc tags.
