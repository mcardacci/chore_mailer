import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from cleaning_sectors import *
import json
import datetime as DT
from datetime import timedelta

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
        sector_dict=self.pick_sector_dict()
        mailing_list=self.mailing_list
        sector=self.sector
        
        for name_initial, sector_int in sector_dict.items():
            for address in mailing_list:
                if address.startswith(name_initial):
                    self.send(address, sector.pick_sector_from_int(sector_int)) 
        
         
    def increment_cycle_int_from_file(self):
        json_file=json.load(open("pattern.json"))
        
        if json_file["cycle_int"] >= 6:
            json_file["cycle_int"]=0

        json_file["cycle_int"]+=1
        
        with open("pattern.json", "w") as f:
            json.dump(json_file, f)

    def pick_sector_dict(self):
        pattern_file=json.load(open("pattern.json"))
        return pattern_file["pattern"][pattern_file["cycle_int"]]

           

# -------------------------- SCRIPT ----------------------
# Date formatting 
today = DT.date.today()


mailer=Mailer(
    subject="Chore List Due Date: {:%m/%d/%Y}".format(today + timedelta(days=14)), 
    password="locationswithpendingfiles",
    mailing_list=("marco.cardacci@gmail.com", "tomworger@gmail.com", "kyle.forbes@gmail.com"),
    from_address="ticketechtest@gmail.com",
    sector=Sector()
)

mailer.send_to_all()
mailer.increment_cycle_int_from_file()
