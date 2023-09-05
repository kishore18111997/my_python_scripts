import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import openpyxl

smtp_server = 'smtp.gmail.com'
smtp_port = 587
gmail_username = 'kishorenate@gmail.com'
gmail_password = 'vjafctsswmelhsdw'

subject = 'Looking for AWS/DevOps role'
message_text = """    Hello HR,

This is kishore, I came to know that you have openings on DevOps role in your company.
I have 3+ years of experience as DevOps engineer from Proxytem Software Services Pvt. Ltd. And I have a keen interest to explore myself in new technologies.
I am a immediate joiner as I am already serving my notice period.
I am very enthusiastic for a opportunity of interview and further discuss for my capability to fit in for the DevOps role.

Please find my attached resume for your reference

Thankyou."""

attachment_path = 'C:\\Users\\User\\Desktop\\my resume\\modified resumes\\resume proxytem\\Kishore 3years.pdf'

excel_file = 'C:\\Users\\User\\Desktop\\my resume\\job-application-mails\\job_mail_list_2.xlsx'
wb = openpyxl.load_workbook(excel_file)
sheet = wb.active

recipients = [row[0].value for row in sheet.iter_rows(min_row=2, max_col=1)]

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(gmail_username, gmail_password)

    for recipient in recipients:
        msg = MIMEMultipart()
        msg['From'] = gmail_username
        msg['Subject'] = subject
        msg['To'] = recipient

        msg.attach(MIMEText(message_text, 'plain'))

        attachment = open(attachment_path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename=attachment.pdf')
        msg.attach(part)

        server.sendmail(gmail_username, recipient, msg.as_string())
        print(f"Email sent to {recipient}")

    server.quit()

except Exception as e:
    print(f"Error: {str(e)}")
