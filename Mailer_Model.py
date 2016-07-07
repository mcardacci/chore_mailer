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
        
email_list=["marco.cardacci@gmail.com", "tomworger@gmail.com", "kyle.forbes@gmail.com"]

duty_sector={
    "one": """
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
            <input type="checkbox" class="list-item" name="animal" value="Cat" />Sweep the floor. <br /> 
            <input type="checkbox" class="list-item" name="animal" value="Dog" />Swiffer the floor<br />
            <input type="checkbox" class="list-item" name="animal" value="Bird" />Wipe down the counter top with cleaning product or soap if none is available.<br />
        </fieldset>
        <!--<script src="strikethrough.js"></script>-->
    </body>
</html>
""",
"two": """
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
            <input type="checkbox" class="list-item" name="animal" value="Cat" />Sweep the floor. <br /> 
            <input type="checkbox" class="list-item" name="animal" value="Dog" />Swiffer the floor<br />
            <input type="checkbox" class="list-item" name="animal" value="Bird" />Wipe down the counter top with cleaning product or soap if none is available.<br />
        </fieldset>
        <!--<script src="strikethrough.js"></script>-->
    </body>
</html>
""",
"three":"""
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
            <input type="checkbox" class="list-item" name="animal" value="Cat" />Sweep the floor. <br /> 
            <input type="checkbox" class="list-item" name="animal" value="Dog" />Swiffer the floor<br />
            <input type="checkbox" class="list-item" name="animal" value="Bird" />Wipe down the counter top with cleaning product or soap if none is available.<br />
        </fieldset>
        <!--<script src="strikethrough.js"></script>-->
    </body>
</html>
"""
}

mailer=Mailer(
"Chore List",
"marco.cardacci@gmail.com",
"ticketechtest@gmail.com",
"locationswithpendingfiles"
)

# mailer.send()
