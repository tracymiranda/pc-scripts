from report import *
import sys

def borderline_talks_with_contention(s):
    return s.std > 1.5 and s.average > 3 and s.average < 4

def disagreement_with_low_vote_count(s):
    return s.std > 1.5 and s.count < 4

def woman_speakers_between_averages(s):
    return s.average >= 3.0 and s.average < 3.5 and s.isWoman

def woman_speakers_high(s):
    return s.average >= 4.0 and s.isWoman

def voted_high_not_accepted(s):
    return s.average >= 4.0 and not s.accepted

def new_predicate(s):
#    return 'cube' in s.body.lower()
#    return 'postgis' in s.body.lower()
    return 'grant' in s.body.lower()

def predicate(s):
    return new_predicate(s)
#    return s.average >= 3.0 and s.average <= 3.5

    #return 'gdal' in s.body.lower()
    #return "geocode" in s.title.lower()
#    return woman_speakers_between_averages(s)
#    return woman_speakers_high(s)
#    return voted_high_not_accepted(s)
#    return s.id == '1412'
#    return disagreement_with_low_vote_count(s)
#    return borderline_talks_with_contention(s)
#    return "Evan Chan" in s.speakers or s.speakers[0].startswith('Eugene') or "GeoMesa" in s.title
    #return "database" in s.tags
    #return s.id == '1466' or s.id == '1471'
#    return s.id == '1517'
#    return 'vector' in s.body.lower() and 'tile' in s.body.lower() and s.average > 3
    #return 'geoserver' in s.body.lower() and s.average > 3
#    return 'transit' in s.body.lower()
#    return 'webgl' in s.body.lower() or 'web gl' in s.body.lower()
#    return 'mapbox' in s.body.lower()

#    return s.id in ['1527', '1522']
#    return s.average >= 3.0 and s.average < 3.5
#    return s.average > 4.0 and not s.accepted
#    return s.average >= 3.0 and not s.accepted
#    return s.status == "Accepted"
#    return  s.company == 'mapbox' and s.accepted
#    return  s.track == 'Academic' and not s.accepted and s.average > 3 and s.isWoman
#    return  "cesium" in s.body.lower()
#    return  'leaflet' in s.title.lower()
    l = [
# Accepted:
# '1607',
# '1481',
# '1526',
# '1430',
# '1385',
# '1471',
# '1472',
# '1460',
# '1432',
# '1487',
# '1437',
# '1496',
# '1477',
# '1377',
# '1455',
# '1422',
# '1391',
# '1517'

# Decline Response:
'1404',
'1516',
'1403',
'1508',
'1490',
'1457',
'1470',
'1514',
'1446',
'1492',
'1493',
#'1399',
'1463'
]
#    return s.id in l
#    return s.accepted and 'remotesensing' in s.tags

#    return 'opendatakit' in s.body.lower()

if __name__ == "__main__":
    S = ALL.standard().filter(lambda s: s.accepted)
    S = S.filter(predicate)
    S.print_subs()
    if 'O' in sys.argv:
        S.open_links()

    if 'L' in sys.argv:
        S.print_links()

    if 'C' in sys.argv:
        S.connect(sys.argv[-1])

    if 'S' in sys.argv:
        S.save_subs('query.results.csv')

    if 'A' in sys.argv:
        S.mark_accepted()
