__author__ = 'dmadden'
import os
import urllib2
import ConfigParser
import smtplib
from email.mime.text import MIMEText

config = ConfigParser.RawConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ip_config.cfg'))

def get_receiving_email():
    try:
        return config.get('info', 'receiving email')
    except:
        return None

def get_ip_config():
    try:
        return config.get("info", "ip")
    except:
        return None

def get_email_password():
    try:
        return config.get('info', 'password')
    except:
        return None

def get_email():
    try:
        return config.get('info', 'email_address')
    except:
        return None

def get_smtp_and_port():
    try:
        smtp = config.get("info", 'smtp-server')
        port = config.get('info', 'port')
        return smtp, port
    except:
        return None

def ip_get(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    html = opener.open(url)
    return html.read()

def send_email(ip):

    sending_email = get_email()
    recieving_email = get_receiving_email()
    subject = "IP ADDRESS CHANGED!"
    body = "The ip address for schroedinger has changed. Please update your DNS records to reflect the new IP: {}".format(ip)

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sending_email
    message['To'] = recieving_email

    con_info = get_smtp_and_port()
    s = smtplib.SMTP(con_info[0], port=con_info[1])

    s.ehlo()
    s.starttls()
    s.login(sending_email, get_email_password())

    s.sendmail(sending_email, [recieving_email], message.as_string())

    s.quit()


def check_ip():
    ip = get_ip_config()
    new_ip = ip_get("http://ipv4bot.whatismyipaddress.com")
    if ip != new_ip:
        send_email(new_ip)


if __name__ == "__main__":
    check_ip()
