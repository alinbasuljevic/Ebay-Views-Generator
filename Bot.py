import requests, time, threading

num_of_views = int(input('Enter the amount of views you would like to generate: '))
ebay_link = input('Enter Item Link: ')

start_time = time.time()

def view_item():
    s = requests.Session()
    visiting_url = s.get(ebay_link)
    
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
    t = threading.Thread(target=view_item)
    t.start()
    print ('Item Viewed Successfully {}/{}'.format(i,num_of_views))
    i += 1

print ('{} Views Successfully Completed in {} seconds!'.format(num_of_views, time.time()-start_time))
    
