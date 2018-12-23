import logging
import smtplib
import time
import json
from argparse import ArgumentParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

CONFIG = None


def send_mail(in_to, in_subject, in_content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(CONFIG['email'], CONFIG['password'])
    msg = MIMEMultipart()
    msg['From'] = CONFIG['email']
    msg['To'] =in_to 
    msg['Subject'] = in_subject

    msg.attach(MIMEText(in_content, 'plain'))

    text = msg.as_string()
    server.sendmail(CONFIG['email'], in_to, text)
    server.quit()


if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument('-c', '--config', required=True)
    ap.add_argument('--to', required=True)
    ap.add_argument('--subj', required=True)
    ap.add_argument('--body', required=True)
    args = ap.parse_args()

    with open(args.config) as config_in:
        CONFIG = json.load(config_in)
    send_mail(args.to, args.subj, args.body)

