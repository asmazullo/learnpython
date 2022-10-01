import os
from email.message import EmailMessage
import ssl
import smtplib

#senha = os.environ.get('GOOGLE_PASS_CELACAVO')
senha = 'votcmdfcoauqzeld'
assunto = 'um ola do seu novo amiguinho virtual'
body =""" oi Mariana, eu sou um robozinho criado pelo Alex.  Vou lancar seus hoarios na sua nova academia em OakBay ta bom ? bjinhos"""
remetente = 'celacavo@gmail.com'
destinatario = 'mlima1708@gmail.com'

en= EmailMessage()
en['From']='testedecaracara@gmail.com'
en['To']=destinatario
en['Subject']=assunto
en.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(remetente, senha)
    smtp.sendmail(remetente, destinatario, en.as_string())
