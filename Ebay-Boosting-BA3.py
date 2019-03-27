import requests, os, time, names, random
import threading

num_of_views = int(input('Enter the amount of views you would like to generate: '))
ebay_link = input('Enter Item Link: ')

start_time = time.time()

def get_item_url():
    s = requests.Session()
    visiting_url = s.get(ebay_link)

def generate_accounts():
    s = requests.Session()
    account_creation_url = 'https://reg.ebay.com/reg/PartialReg'
    account_start = s.get(account_creation_url, headers=headers)
    payload = {
        'isSug': 'false',
        'countryId': '1',
        'userid':'', 
        'ru': 'http://www.ebay.com',
        'firstname': names.get_first_name(),
        'lastname': names.get_last_name(),
        'email': 'randomguty+{}@gmail.com'.format(random.randint(1,1000)),
        'PASSWORD': 'Soccerdude104',
        'promotion': 'true',
        'iframeMigration1': 'true',
        'mode': '1',
        'frmaction': 'submit',
        'tagInfo': 'ht5%3DAQAAAWlLJlj8AAUxNjk1MGRjODFiYi5hYjZhODZhLjZlZjBkLmZmZmZmODRmDU0X%252Fi4kiYYJAVYcvxeIvPove18*%7Cht5new%3Dfalse%26usid%3D5185a3b81690ac19c1f43109ffffe910',
        'hmvb':'', 
        'isGuest': '0',
        'idlstate': '',
        'profilePicture': '',
        'agreement': 'Terms and conditions',
        'signInUrl': 'https%3A%2F%2Fwww.ebay.com%2Fsignin%3Fsgn%3Dreg%26siteid%3D0%26co_partnerId%3D0%26UsingSSL%3D1%26rv4%3D1%26regUrl%3Dhttps%253A%252F%252Freg.ebay.com%252Freg%252FPartialReg%253Fsiteid%253D0%2526co_partnerId%253D0%2526UsingSSL%253D1%2526rv4%253D1',
        'personalFlag': 'true',
        'isMobilePhone': '',
        '_trksid': 'p2052190',
        'ets': 'AQADAAAAEGyDxaYRWeCsNwfMOIs91Yo'
    }
    headers = {
        'dnt': '1',
        'origin': 'https://reg.ebay.com',
        'referer': 'https://reg.ebay.com/reg/PartialReg?siteid=0&co_partnerId=0&UsingSSL=1&rv4=1&signInUrl=https%3A%2F%2Fwww.ebay.com%2Fsignin%3Fsgn%3Dreg%26siteid%3D0%26co_partnerId%3D0%26UsingSSL%3D1%26rv4%3D1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
    creation_request = s.post(url, data=payload, headers=headers)
    print (creation_request.status_code)



for i in range(num_of_views):
    t = threading.Thread(target=get_item_url)
    t.start()
    print ('Item Viewed Successfully {}/{}'.format(i,num_of_views))
    i += 1

print ('{} Views Successfully Completed in {} seconds!'.format(num_of_views, time.time()-start_time))
    
