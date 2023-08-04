# %%
import smtplib, ssl

# %%
port = 587
gwdg_server = "email.gwdg.de"
# server = smtplib.SMTP(gwdg_server,port=port)
# server.noop()
receiver_email = "dhirajupadhyay01@gmail.com"
sender_email = "dhiraj.kumar@gwdg.de"
# password = input("Input Password")
password = "God!@12forgive"

message = """\
Subject: Hi there

This message is sent from Python as a test.
"""

context = ssl.create_default_context()
with smtplib.SMTP(gwdg_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

# %%
context = ssl.create_default_context()
server = smtplib.SMTP_SSL("email.gwdg.de", port=465, context=context)
server.noop()
