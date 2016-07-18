import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from cleaning_sectors import *
import json

class Mailer(object):

    def __init__(self, **args):
        self.subject=args.get('subject', "Default Subject") 
        self.mailing_list=args.get('mailing_list', "email@email.com")
        self.from_address=args.get('from_address', "email@amil.com")
        self.password=args.get('password', "password")
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

    def increment_cycle_int_from_file(self):
        json_file=json.load(open("pattern.json"))
        
        if json_file["cycle_int"] >= 6:
            json_file["cycle_int"]=0

        json_file["cycle_int"]+=1
        
        with open("pattern.json", "w") as f:
            json.dump(json_file, f)
# -------------------------- TESTING ----------------------

mailer=Mailer(
    subject="TEST Chore List", 
    password="locationswithpendingfiles",
    mailing_list=("marco.cardacci@gmail.com", "tomworger@gmail.com", "kyle.forbes@gmail.com"),
#    mailing_list=("marco.cardacci@gmail.com", "kyle.forbes@gmail.com"),
    from_address="ticketechtest@gmail.com",
    sector=Sector()
)

mailer.increment_cycle_int_from_file()
# mailer.send_to_all()
