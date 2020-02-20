import re
from collections import Counter

def readlogfile(filename):
    with open(filename) as f:
        logfile = f.read()
        return logfile

def logparsing(logfile):
    regex=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    matchexpression=re.findall(regex, logfile)
    return matchexpression

def counting_ips(matchexpression):
    count_ips = Counter(matchexpression)
    print(count_ips)

if __name__=='__main__':
    counting_ips(logparsing(readlogfile('access_log')))
