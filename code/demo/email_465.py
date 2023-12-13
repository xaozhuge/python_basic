import smtplib
import imaplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 获取环境变量-邮箱配置
smtp_server = os.getenv("EMAIL_SMTP_SERVER")
imap_server = os.getenv("EMAIL_IMAP_SERVER")
# 你的发件人邮箱
username = os.getenv("EMAIL_USERNAME")
# 你的发件人邮箱密码或应用程序专用密码
password = os.getenv("EMAIL_PASSWORD")
to_email = os.getenv("TO_EMAIL")

# 创建邮件对象
message = MIMEMultipart()
message["From"] = username
message["To"] = to_email
message["Subject"] = "666主题：这是一封测试邮件"
# 邮件正文
body = "666你好，这是一封使用Python发送的测试邮件。"
message.attach(MIMEText(body, "plain"))

# 发送邮件
with smtplib.SMTP_SSL(smtp_server, 465) as server:
    # 登录到发件人邮箱
    server.login(username, password)
    # 将邮件发送到收件人邮箱
    server.send_message(message)

# 将邮件保存到"发件箱"
with imaplib.IMAP4_SSL(imap_server) as imap_server:
    imap_server.login(username, password)
    imap_server.append('Sent', '\\Seen', imaplib.Time2Internaldate(time.time()), message.as_string().encode('utf-8'))
    imap_server.logout()

print("邮件发送成功")


'''
docker exec python380_c python3 demo/email_465.py
'''