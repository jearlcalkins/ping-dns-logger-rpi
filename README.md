# ping-dns-logger-rpi
1 second ping and dns reverse lookup logging for the raspberry pi, given 1 minute granular cron

the application is written in python 3

##### raspberry pi environment
Raspberry Pi 3 Model B Plus Rev 1.3
Raspbian GNU/Linux 9 (stretch)
Python 3.5.3
connectivity is via ethernet eth0

##### requirement / ask
I have a need to test network connectivity and DNS functionality, every second, for long periods of time.  The rpi's raspbian OS cron is only granular to running processes, by the minute.  This application can be cron'd to run every minute, but will execute a ping, a reverse DNS lookup, and log the result every second.  The application does not run past the minute, noting cron will start yet another process at the top of the next minute.

##### how-to run the application
```
pi@pi:~ $ python3 pingNdnsLogger.py  172.217.12.14  205.171.2.25
2020-03-09 19:43:06.762464 ,pinged, 172.217.12.14 , 25.6 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:07.864319 ,pinged, 172.217.12.14 , 25.0 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:08.963607 ,pinged, 172.217.12.14 , 25.9 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:10.065247 ,pinged, 172.217.12.14 , 25.1 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:11.165448 ,pinged, 172.217.12.14 , 25.1 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:12.266455 ,pinged, 172.217.12.14 , 25.0 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:13.366581 ,pinged, 172.217.12.14 , 25.6 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:14.468159 ,pinged, 172.217.12.14 , 25.6 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:15.569607 ,pinged, 172.217.12.14 , 25.1 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:16.670237 ,pinged, 172.217.12.14 , 25.8 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:17.771978 ,pinged, 172.217.12.14 , 25.4 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:18.919963 ,pinged, 172.217.12.14 , 25.3 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:20.021286 ,pinged, 172.217.12.14 , 25.1 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:21.121436 ,pinged, 172.217.12.14 , 25.9 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:22.223006 ,pinged, 172.217.12.14 , 25.4 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:23.346097 ,pinged, 172.217.12.14 , 25.8 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:24.450298 ,pinged, 172.217.12.14 , 25.3 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:25.565287 ,pinged, 172.217.12.14 , 25.3 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:26.688743 ,pinged, 172.217.12.14 , 25.8 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:27.842273 ,pinged, 172.217.12.14 , 25.5 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:28.983635 ,pinged, 172.217.12.14 , 25.5 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:30.134384 ,pinged, 172.217.12.14 , 25.7 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:31.279280 ,pinged, 172.217.12.14 , 25.8 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:32.422629 ,pinged, 172.217.12.14 , 25.2 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:33.576840 ,pinged, 172.217.12.14 , 26.5 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:34.732287 ,pinged, 172.217.12.14 , 26.2 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:35.876105 ,pinged, 172.217.12.14 , 33.5 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:37.039678 ,pinged, 172.217.12.14 , 26.1 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:38.182385 ,pinged, 172.217.12.14 , 25.5 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:39.338457 ,pinged, 172.217.12.14 , 25.7 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:40.482072 ,pinged, 172.217.12.14 , 25.7 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:41.634361 ,pinged, 172.217.12.14 , 25.7 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:42.781283 ,pinged, 172.217.12.14 , 26.2 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:43.924255 ,pinged, 172.217.12.14 , 26.5 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:45.075188 ,pinged, 172.217.12.14 , 26.5 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:46.232253 ,pinged, 172.217.12.14 , 25.6 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:47.382752 ,pinged, 172.217.12.14 , 26.4 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:48.539400 ,pinged, 172.217.12.14 , 26.8 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:49.696606 ,pinged, 172.217.12.14 , 25.6 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:50.853865 ,pinged, 172.217.12.14 , 26.5 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:52.006444 ,pinged, 172.217.12.14 , 26.5 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:53.163194 ,pinged, 172.217.12.14 , 26.5 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:54.316798 ,pinged, 172.217.12.14 , 26.3 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:55.461564 ,pinged, 172.217.12.14 , 25.4 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:56.613505 ,pinged, 172.217.12.14 , 25.3 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:57.766285 ,pinged, 172.217.12.14 , 26.9 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:43:58.912466 ,pinged, 172.217.12.14 , 25.5 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:44:00.049859 ,pinged, 172.217.12.14 , 25.3 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:44:01.201891 ,pinged, 172.217.12.14 , 26.0 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:44:02.342944 ,pinged, 172.217.12.14 , 25.6 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:44:03.444087 ,pinged, 172.217.12.14 , 25.3 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net
2020-03-09 19:44:04.571062 ,pinged, 172.217.12.14 , 25.8 ,DNSsuccessfullyreversed, den02s02-in-f14.1e100.net

