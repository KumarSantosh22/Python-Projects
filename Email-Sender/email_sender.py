import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('./index.html').read_text())

email = EmailMessage()
email['from'] = 'Santosh Kumar'
email['to'] = 'shkr2209@gmail.com'
email['subject'] = 'python email script'

text = 'Hi, I am a python Developer'

# email.set_content(text)
email.set_content(html.substitute({'name':'SANTOSH'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<your e-mail>', '<your password>')
    smtp.send_message(email)
    print('email sent')