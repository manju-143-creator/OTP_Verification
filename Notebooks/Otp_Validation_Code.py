import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart   # importing all neseccary modules for creating mail
import random # import random module to create unique passwordt
def generate_otp(letters,numbers,special_charater):
  otp=[]
  for i in range(1,3):               #loop is to create in each time to create unique password for security purpose with combination of lettter,numbers
    i=random.choice(letters)
    otp.append(i)
    i=random.choice(numbers)
    otp.append(i)
    i=random.choice(special_charater)
    otp.append(i)
    result = ''.join(map(str, otp))  #password store in list format so i need to merge so, i used join for combine
  return result
letter = ['A', 'B', 'C', 'D', 'F', 'G','H', 'I', 'J', 'K']
number=[1,2,3,4,5,6,7,8,9,0]
special_charater=['@','&','*','#']
k=generate_otp(letter,number,special_charater)


smtp_server = 'smtp.gmail.com'  #  SMTP server address it depends upon which account to be used
port = 587  # Port may vary depending on your SMTP server
sender_email = 'manjunadha865@gmail.com'  # email address
password = 'mhbjevpwnqjnkxll' #password
# Create a message
message = MIMEMultipart() #for creating message to import this module
message['From'] = sender_email
message['To'] = 'amitimanju76@gmail.com'  # recipient's email address
message['Subject'] = 'Hello, there!'
from email.mime.text import MIMEText
# Create MIMEText object for the body
body = "Hi, this is your a one time password: "+k+" Enter to access" # here i added OTP Along with body message
body_part = MIMEText(body, 'plain')
message.attach(body_part)

server=smtplib.SMTP(smtp_server, port) # connect with sender account
server.starttls()  # Secure the connection
server.login(sender_email, password) # login to account

text = message.as_string()
server.sendmail(sender_email,'amitimanju76@gmail.com', text)
server.quit()
print('Succesfully Send mail...')
n=3
while n>0:
  otp=input('enter otp')
  if otp==k:
    print('Grant Access')
    break
  else:
    n=n-1
    print(f"you have {n} attempts left")
    if n==0:
      print('Access denied try again')