import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from cleaning_sectors import *
import json

class Mailer(object):

    def __init__(self, **args):
        self.subject=args.get('subject', None) 
        self.mailing_list=args.get('mailing_list', None)
        self.from_address=args.get('from_address', None)
        self.password=args.get('password', None)
        self.sector=args.get('sector', "There is a problem with the HTML")
        
    def send(self,to_address,content):
        msg=MIMEMultipart()
        msg['To']=to_address
        msg['From']=self.from_address
        msg['Subject']=self.subject
        
        msg.attach(MIMEText(content,'html'))
        
        mail=smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo() # this isn't in the example
        mail.starttls()
        mail.login(self.from_address,self.password)
        text=msg.as_string()
        mail.sendmail(self.from_address, to_address,text)
        mail.close()
    
    def send_to_all(self):
        mailing_list=self.mailing_list
        sector=self.sector
        for address in mailing_list:
             self.send(address,sector.one())

# -------------------------- TESTING ----------------------

mailer=Mailer(
    subject="TEST Chore List", 
    password="locationswithpendingfiles",
#    mailing_list=("marco.cardacci@gmail.com", "tomworger@gmail.com", "kyle.forbes@gmail.com"),
    mailing_list=("marco.cardacci@gmail.com", "kyle.forbes@gmail.com"),
    from_address="ticketechtest@gmail.com",
    sector=Sector()
)

p=json.load(open("pattern.json"))
print p["pattern"]["cycle_int"]["m"]
# mailer.send_to_all()
