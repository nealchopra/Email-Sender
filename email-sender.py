from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'you@company.com' #add your email
email_password = 'password'     #see README.md
email_receiver = 'yourfriend@company.com' #add the email of the person you want to send the email to

subject = "Checking In!"
body = """
Hey [Friend],

I hope this email finds you well! It's been a while since we last caught up and I just wanted to check in and see how you're doing.

I'm doing well, just keeping busy with work and trying to stay healthy. I've been enjoying spending time with my family and taking some long walks to clear my head.

How about you? What have you been up to lately? I'd love to hear all about it.

Take care and stay safe.

Best,
[Your Name] 
""" #make sure to change [Friend] to the person you are sending it to and [Your Name] to your name!

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())



