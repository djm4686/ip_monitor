# ip_monitor
A simple cron script for detecting if the dynamic IP changed on the running system.

In order for this to work, a config file named "ip_config.cfg" needs to be placed in the same directory as monitor.py.

The cfg should look like:

[info]

\# old or current ip

ip = 76.28.16.85

\#Email address to send the alert

email_address = ****@****

\#Password for email address

password = ***** 

\#Email to recieve the alert

receiving-address = ****@****

smtp-server = smtp.gmail.com

port = 587
