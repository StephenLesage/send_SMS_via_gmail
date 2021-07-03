'''
If an error is raised, visit:
https://www.google.com/settings/security/lesssecureapps
and change:
'Allow less secure apps'
to 
'ON'
'''

import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

############################################################################################
################################# Enter Specifics of User ##################################
############################################################################################

# server login info
email_info = ['John_Doe@gmail.com','John_Doe_email_password']

# sender info
sender_info = ['John Doe']

# contacts list
contacts_list = {
				 1: {'name': 'John Doe',    'number': 'XXXXXXXXXX', 'carrier': 'att'    },
				 2: {'name': 'Jane Doe',    'number': 'XXXXXXXXXX', 'carrier': 'verizon'}
				}
############################################################################################
############################################################################################
############################################################################################

def message_info(contacts_list):

	# parse contacts list
	keys = contacts_list.keys()

	# print contacts list
	print('\n-- CONTACTS LIST --\n')
	for key in keys:
		print(str(key)+': '+contacts_list[key]['name'])

	# prompt user to select contact from contacts list
	user_input = int(input('\nSelect contact:\n'))

	# check user input
	if user_input <= key and user_input >= 1:
		good_input = True 
	else:
		good_input = False

	# if bad user input print again until good user input
	while good_input == False:

		# print contacts list
		print('\n-- CONTACTS LIST --\n')
		for key in keys:
			print(str(key)+': '+contacts_list[key]['name'])

		# prompt user to select contact from contacts list
		print('\nBad input. Try again.')
		user_input = int(input('Select contact:\n'))

		# check user input
		if user_input <= key and user_input >= 1:
			good_input = True 
		else:
			good_input = False

	# SMS contact info
	contact_info = contacts_list[int(user_input)]

	# SMS subject
	subject = str(input('\nEnter SMS subject:\n'))

	# SMS message
	message = str(input('\nEnter SMS message:\n'))

	return( contact_info, subject, message )

# mobile carriers list
mobile_carriers = {'att': '@txt.att.net',
				   'sprint': '@messaging.sprintpcs.com',
				   'verizon': '@vtext.com',
				   'cricket': '@mms.cricketwireless.net',
				   'tmobile': '@tmomail.net',
				   'metropcs': '@mymetropcs.com',
				   'spectrum': '@vtext.com',
				   'boostmobile': '@sms.myboostmobile.com'}

# retrieve server login info
email, password = email_info

# retrieve SMS info
contact_info, sms_subject, sms_body = message_info(contacts_list)

# parse contact info to be sent to server
mobile_carrier_keys = mobile_carriers.keys()
for key in mobile_carrier_keys:
	if contact_info['carrier'] == key:
		send_sms_to = contact_info['number'] + mobile_carriers[key]

# gmail server info
smtp = "smtp.gmail.com" 
port = 587

# initialize server
server = smtplib.SMTP(smtp, port)

# open server sonnection
server.starttls()

# login to server
server.login(email, password)

# structure message
msg = MIMEMultipart()

# fill in SMS info
msg['From'] = sender_info[0]
msg['To'] = send_sms_to
msg['Subject'] = sms_subject + '\n'
msg.attach( MIMEText( sms_body, 'plain' ) )

# convert SMS from <byte> to <string>
sms = msg.as_string()

# send SMS
print('\nSending SMS ... ')
server.sendmail( email, send_sms_to, sms )
print('SMS sent.')

# close server connection
server.quit()


