import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from variable import email_pass
from stringbuilder import stringbuilder

def mailsender (order_summary):
    mail_content = stringbuilder(order_summary)
   
    #The mail addresses and password
    sender_address = 'chlmqst@gmail.com'
    sender_pass = email_pass
    receiver_address = 'carl@dwsprinting.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = f"SO#{order_summary['sales_order_number']} Completed"   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')