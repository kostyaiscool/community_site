from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config
import smtplib

smtp_server = smtplib.SMTP(config.EMAIL_HOST, config.EMAIL_HOST_PORT)
smtp_server.starttls()
smtp_server.login(config.EMAIL_HOST_USER, config.EMAIL_HOST_PASSWORD)

# Создание объекта сообщения
msg = MIMEMultipart()

# Настройка параметров сообщения
msg["From"] = config.EMAIL_HOST_USER
msg["To"] = "yanubtitrupzaeal@gmail.com"
msg["Subject"] = "Тестовое письмо 📧"

# Добавление текста в сообщение
text = "Привет! Это тестовое письмо, отправленное с помощью Python 😊"
msg.attach(MIMEText(text, "plain"))

# Отправка письма
smtp_server.sendmail(config.EMAIL_HOST_USER, "yanubtitrupzaeal@gmail.com", msg.as_string())

# Закрытие соединения
smtp_server.quit()