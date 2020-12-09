import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()#for gmail encription
from_msg='jyotipalariya1997@gmail.com'
to_msg='jyoti.palariya.311997@gmail.com'
server.login(from_msg,'fqouqprgjmorvcmt')#this password u will get by allowing 2 step authentication on ur mail id and then pass generate also u can
                                                                #distroy this password nytime u want
message="Hi there, message from Python"
server.sendmail(from_msg,to_msg,message)
server.quit()