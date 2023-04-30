#!/usr/bin/python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os , click 

def main():
   print("program running ...")
   send_email()

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--subject', '-s',envvar='SUBJECT',help='Subject of email')
@click.option('--fromto','-f',nargs=1,envvar='FROMTO',help='email from example@gmail.com')
@click.option('--to','-t',nargs=1,envvar='TO',help="send email to AAA@example.com")
@click.option('--message_text','-m',envvar='MESSAGETXT',help="send message as plain text")
@click.option('--message_html','-M',envvar='MESSAGEHTML',help="send message as HTML")
@click.option('--login','-l',envvar="LOGIN",nargs=1,help="login email of gmail example : user@gmail.com")
@click.option('--password','-p',envvar="PASSWORD",nargs=1,help="password of your gamil generated from App passwords")
@click.option('--sendto','-st',multiple=True,default=[],envvar='SENDTO',help="send email to multiple email ")

def send_email(subject,fromto,to,message_text,message_html,login,password,sendto):
    """Tool to send  emails by GMAIL"""
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = fromto
    message['To'] = to

    message.attach(MIMEText(message_text, 'plain'))
    message.attach(MIMEText(message_html, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(login, password)
    for recipient in sendto:
        server.sendmail(fromto, recipient, message.as_string())
    server.quit()
    click.echo(click.style("Done",fg='green'))    
# example of message as text and html
#message1 = MIMEText('# A Heading\nSomething else in the body', 'plain')
#message2 = MIMEText('<h1 style="color: blue">A Heading</a><p>Something else in the body</p>', 'html')
if __name__ == '__main__':
   os.system('clear')
   main()
