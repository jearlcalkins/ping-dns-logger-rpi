import datetime 
from datetime import timedelta
import time
import re
import argparse
import subprocess

"""
Created on Mon Feb 26 15:40:07 2018
@author: Jeff Calkins 
@license: MIT-license
This file contains the pingDns logger for raspberry Pi
"""
# the pingit function uses the operating system's ping application
# the ping is configured to; only ping once, to timeout after 3
# seconds and not to use the DNS, to find the IP's FQDN (name)
# if successful, the time in ms will be logged, noting it was "pinged"
# if the ping fails, the log will note "pingfailure"

def pingit(theIp):

    cmd = ["ping", "-c", "1", "-W", "3", "-n", theIp]
    result = subprocess.run(
         cmd,
         stdout=subprocess.PIPE
    )
    if result.returncode != 0:
        print("pingfailure,", datetime.datetime.now(), end = '')
        return

    r = result.stdout.decode('utf-8')
    p = re.compile(r'^.+time=([^ ]+) ms')
    #64 bytes from 97.122.221.193: icmp_seq=1 ttl=62 time=32.5 ms
    for line in r.split('\n'):
        res = p.search(line)
        if res:
            print("pinged,", theIp, ",", res.group(1), ",", end = '' )

# the reverseDns function uses a specif DNS, usually the ISPs, to reverse
# lookup the IP address for its FQDN (fully qualified domain name)
# the conversation with the DNS, in itself a connectivity test and it
# validates an ISPs DNS infrastructure is functioning.
# a logged dnsfailure can note the DNS and the network has failed

def reverseDns(theIp, theDns):

    cmd = ["nslookup", theIp, theDns]
    result = subprocess.run(
         cmd,
         stdout=subprocess.PIPE
    )
    if result.returncode != 0:
        print("dnsfailure,", datetime.datetime.now(), end='' )
        return

    r = result.stdout.decode('utf-8')
    p = re.compile(r'^.+name = (.+)\.$')
    # 193.221.122.97.in-addr.arpa       name = 97-122-221-193.hlrn.qwest.net.
    for line in r.split('\n'):
        res = p.search(line)
        if res:
            print("DNSsuccessfullyreversed,", res.group(1), end='')

# parse the python run line for an IP address (IPV4)
parser = argparse.ArgumentParser()
parser.add_argument("ipaddr", help="the ip addr we ping", type=str)
parser.add_argument("favDns", help="which DNS do we use", type=str)
args = parser.parse_args()
theIP = args.ipaddr
favDns = args.favDns

# this python 3 application runs on a limited compute resource, 
# raspberry pi 3.  the linux cronjob is limited to starting a new 
# process, every minute
# 
# the application will ping an IPv4 device, use a specific ISP's DNS
# to reverse lookup the IP, finding the FQDN (name).  the application
# processing and loop takes longer than a second to process a sample.
# there is a 1 second sleep between the pnging and dns conversation, 
# an attempt to sample every second.  The processing loop allows the
# processing 2 seconds short of 1 minute
#
# the application can be run from the commandline and will ping / dns 
# communicate, roughly, every second.  The logging application is
# intended to be run every minute, started by the operating system
# cron and the STDOUT results should be appended to a log file.  in
# the event there is an outage, the log file will note the event and
# the outage duration can be calculated.
# to run the application, pass the IP to ping and which DNS to use:
# python3 posv2.py 192.168.0.99 205.171.2.25
#
# the following cron line will run every minute, during every hour, 
# during all months and any day of week. the application will run
# short of one minute, logging short of 60 ping - dns samples.
#
# * * * * * python3 /home/pi/posv2.py 192.168.0.99 205.171.2.25 >> pingNdnsLogging.txt

# hardcode the DNS below, the application will use this DNS to 
# reverse lookup resolve your IP's name
# btw, one of google's DNS is '8.8.8.8'
# "205.171.2.25" a centurylink DNS

strtime = datetime.datetime.now()
endtime = strtime + timedelta(seconds=58)  
print(strtime,",", end='')
pingit(theIP)
reverseDns(theIP,favDns)
print("")
time.sleep(1)
strtime = datetime.datetime.now()

while (endtime > strtime) :
    print(strtime,",", end='')
    pingit(theIP)
    reverseDns(theIP,favDns)
    print("")
    time.sleep(1)
    strtime = datetime.datetime.now()
