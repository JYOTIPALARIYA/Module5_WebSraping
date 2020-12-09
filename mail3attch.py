# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# from_add='jyotipalariya1997@gmail.com'
# to_add='jyoti.palariya.311997@gmail.com'
# subject='Mail from Python Script'

# msg=MIMEMultipart()
# msg['From']=from_add
# msg['To']=to_add
# msg['Subject']=subject

# body="Hey there! Sending mail through Python!"
# msg.attach(MIMEText(body,'plain'))
# message=msg.as_string()


# server=smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()#for gmail encription

# server.login(from_add,'fqouqprgjmorvcmt')#this password u will get by allowing 2 step authentication on ur mail id and then pass generate also u can

# server.sendmail(from_add,to_add,message)
# server.quit()





'''----------------------------Html text'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



def send(filename):
    from_add='jyotipalariya1997@gmail.com'
    to_add='jyoti.palariya.311997@gmail.com'
    subject='Finace Report'

    msg=MIMEMultipart()
    msg['From']=from_add
    msg['To']=to_add
    msg['Subject']=subject

    body="<b>Hey there! Finance Report Attach!<b>"
    msg.attach(MIMEText(body,'html'))

    # my_file=open("scrap.csv",'rb')
    my_file=open(filename,'rb')
    part=MIMEBase('application','octat-stream')#to obey straet to upload our file
    part.set_payload((my_file).read())
    encoders.encode_base64(part)#to encode our attchment using base64 scheme
    # part.add_header('Content-Disposition','attachment; filename= '+ 'scrap.csv')
    part.add_header('Content-Disposition','attachment; filename= '+ filename)
    
    msg.attach(part)
    message=msg.as_string()


    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()#for gmail encription

    server.login(from_add,'fqouqprgjmorvcmt')#this password u will get by allowing 2 step authentication on ur mail id and then pass generate also u can

    server.sendmail(from_add,to_add,message)
    server.quit()