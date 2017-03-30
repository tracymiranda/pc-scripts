import os
import yaml
from subprocess import call
import urllib

YEAR = 2016

if __name__ == "__main__":
    p = os.path.join(os.path.expanduser('~'), ".foss4g")
    f = yaml.load(open(p, 'r'))
    usr =  urllib.quote_plus(f['user'])
    pwd =  urllib.quote_plus(f['pwd'])

    cmd = ['wget',
           '--save-cookies', 'cookies.txt',
           '--post-data', 'name=%s&pass=%s&form_build_id=form--wyE7ecVE7aujFTM9ylmm-fIRruT1qmVuEqTDoRtGEc&form_id=user_login&op=Log+in' % (usr, pwd),
           'https://%d.foss4g-na.org/user/login' % YEAR]

    call(cmd)

    os.remove("./login")

    cmd = ['wget',
           '--load-cookies', 'cookies.txt',
           '-O', 'submissions.csv',
           'https://%d.foss4g-na.org/pc-admin/sessions/eclipsecon-admin-unprocessed.csv?order=value_2&sort=asc' % YEAR]
    call(cmd)

    cmd = ['wget',
           '--load-cookies', 'cookies.txt',
           '-O', 'community-votes.csv',
           'https://%d.foss4g-na.org/community-voting/report.csv' % YEAR]
    call(cmd)
