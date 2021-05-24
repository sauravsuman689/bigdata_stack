import sys
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart  import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import argparse
import getpass

parser = argparse.ArgumentParser()

parser.add_argument('--total_broker', required=True, help="Pass the total no. of brokers in the Kafka Cluster")
parser.add_argument('--zk_host_name', required=True, help="Pass any one zookeeper server of this cluster")
parser.add_argument('--env', required=True, help="Pass the environment name of the cluster")

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

total_broker = args.total_broker
zk_host_name = args.zk_host_name
env = args.env

zkcli="/Users/sauravsuman/saurav/softwares/zookeeper/bin/zkCli.sh"
zk_port=2181

def check_broker():

    cmd = f'{zkcli} -server {zk_host_name}:{zk_port} ls /brokers/ids | tail -1 | sed "s/[][]//g" | tr -d "," | tr " " "\n" | wc -l'

    available_broker = subprocess.getoutput(cmd)

    if total_broker != available_broker:
        #print(f"{env} : Only {available_broker} brokers are connected out of {total_broker} , Please check..!")
        send_message = f"{env} : Only {available_broker} brokers are connected out of {total_broker} , Please check..!"
        send_email(send_message)

    else:
        #print(f"{env} : All brokers are connected")
        send_message = "{env} : All brokers are connected"
        send_email(send_message)

## Email Function

def send_email(content):

    send_from_email = 'no-reply@localhost.com'
    send_to_email = ['xyz@gmail.com']
    subject = f'{env} : Kafka Broker Connection Report'

    msg = MIMEMultipart()
    msg['From'] = send_from_email
    msg['To'] = ', '.join(send_to_email)
    msg['Subject'] = subject

    msg.attach(MIMEText(content, 'plain'))

    google_tls_port = 587
    #port = 10255

    password = getpass.getpass(prompt='Please enter you gmail password: ')

    server = smtplib.SMTP('smtp.gmail.com', google_tls_port)
    #server = smtplib.SMTP('localhost', port)
    server.starttls()
    server.login("xyz@gmail.com", password)
    text = msg.as_string()
    server.sendmail(send_from_email, send_to_email, text)
    server.quit()


if __name__ == '__main__':
    check_broker()

