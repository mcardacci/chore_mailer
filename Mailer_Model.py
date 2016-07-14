import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Mailer(object):

    def __init__(self, **args):
        self.subject=args.get('subject', None) 
        self.to_address=args.get('to_address', None)
        self.mailing_list=args.get('mailing_list', None)
        self.from_address=args.get('from_address', None)
        self.password=args.get('password', None)
        print args
        
    def send(self,content):
        msg=MIMEMultipart()
        msg['From']=self.from_address
        msg['To']=self.to_address
        msg['Subject']=self.subject
        
        msg.attach(MIMEText(content,'html'))
        
        mail=smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo() # this isn't in the example
        mail.starttls()
        mail.login(self.from_address,self.password)
        text=msg.as_string()
        mail.sendmail(self.from_address,self.to_address,text)
        mail.close()
    
    def format_content(self):
        pass
   
    def send_to_all(self, mailing_list):
        pass

# -------------------------- TESTING ------------------------------

mailer=Mailer(
    subject="Chore List", 
    password="locationswithpendingfiles",
    to_address="marco.cardacci@gmail.com",
    mailing_list=("marco.cardacci@gmail.com", "tomworger@gmail.com", "kyle.forbes@gmail.com"),
    from_address="ticketechtest@gmail.com",
    )


# mailer.send()
