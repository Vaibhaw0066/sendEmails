import smtplib
from email.message import EmailMessage



email=EmailMessage()
email['from']='Kumar Vaibhaw'
email['to']='sunilvashist45@gmail.com'
email['Subject']='I am Sunil!'
email.set_content('I am a Jaadugar ')





with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    # smtp.noop()
    smtp.starttls()
    smtp.login('vaibhawtesting@gmail.com','Vaibhaw@123')
    smtp.send_message(email)
    print('Mail sent !')