import smtplib
import csv
import time
from os import system, name
from file import fulltext, SUBJECT



def clear():
	if name=='nt':
		_ = system('cls')
	else:
		_ = system('clear')

clear()
print("Ensure you have saved your database file in the .csv format in this very directory!")
time.sleep(5)
db = "./emails.csv"
email = "yourEmail"
password = "yourAppPass"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)

with open(''+db+'') as data:
	row = csv.DictReader(data)
	for line in row:
		name = line['fullname']
		TEXT = "Hi "+name+"! "+fulltext
		msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
		add = line['email']
		server.sendmail(email, add, msg)
		print("Mail sent to "+name+"")

server.quit()