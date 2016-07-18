
import httplib
import re



def get_hsts( url, user_agent ):
	[proto, aux, hostname] = url.split("/")
	try:
		if proto == "https:":
			conn = httplib.HTTPSConnection(hostname, timeout=5)
		else:
			conn = httplib.HTTPConnection(hostname, timeout=5)
		conn.putrequest("GET", "/", skip_host=True)
		conn.putheader("Host", hostname)
		conn.putheader("User-Agent", user_agent)
		conn.endheaders()
		res = conn.getresponse()
	except:
		return
	if res.getheader('strict-transport-security'):
		return True
	else:
		return False

print "magaliti\t->\tURL : https://saite.ge"
url = raw_input('URL : ')
urlre = re.compile('http(s)?://[a-zA-Z0-9.-]+(\:[0-9]+)?$')
if not url or not urlre.match(url):
        print "shecdomaa url -shi"
        exit()

user_agent = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"
output = get_hsts( url, user_agent )

if output:
	print "HSTS ayeni"
else:
	print "ar ayenia HSTS"
