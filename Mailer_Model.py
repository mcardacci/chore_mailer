import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Mailer(object):

    def __init__(self,subject,to_address,from_address,password):
        self.subject=subject
        self.to_address=to_address
        self.from_address=from_address
        self.password=password

    def format_content(self):
        pass
    
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
        
mailer=Mailer(
"Chore List",
"marco.cardacci@gmail.com",
"ticketechtest@gmail.com",
"locationswithpendingfiles"
)

mailer.send("""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">          
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <title>Chore List</title>
        <link rel="stylesheet" href="stylesheet.css" type="text/css">
    </head>
    <body>
        <fieldset>
            <legend>
                Have you done your Chores this Week?
            </legend>
            <input type="checkbox" name="animal" value="Cat" />Cats <br />                         
            <input type="checkbox" name="animal" value="Dog" />Dogs<br />                         
            <input type="checkbox" name="animal" value="Bird" />Birds<br />                         
        </fieldset>
    </body>
</html>
""")
