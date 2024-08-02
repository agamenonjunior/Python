'''
pip install secure-smtplib
'''
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(destinatario, assunto, mensagem):
    
    #CONFIGURAÇÃO DO SERVIDOR DE E-MAIL
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    remetente = 'remetente@gmail.com'
    senha = 'senha do email'

    #CRIANDO A MENSAGEM
    msg = MIMEMultipart()
    msg['From']    = remetente
    msg['To']      = destinatario
    msg['Subject'] = assunto

    #CORPO DA MENSAGEM
    msg.attach(MIMEText(mensagem, 'plain'))

    try:
        #CONECTANDO COM O SERVIDOR SMTP
        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls() # TLS
        server.login(remetente,senha) # Login SMTP

        #REALIZANDO O ENVIO DO E-MAIL
        server.sendmail(remetente,destinatario, msg.as_string())
        print('E-mail enviado com Sucesso ! ')
    
    except Exception as e:
        
        print("error ao enviar o E-mail{e}")
    
    finally:

        #ENCERRANDO A CONEXAO COM SERVIDOR
        server.quit() 
