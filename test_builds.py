import requests
import json
import time
re=requests.Session()
def tt():
    return str(int(time.time()*1000))
def tl():
    return str(int(time.time()))
class Test_Builds():
    def builds():
        #protocol 1
        cook=(re.get('https://www.irctc.co.in').headers)['Set-Cookie']
        #protocol 2
        (re.get('https://www.irctc.co.in/nget/').headers)
        #json found
        json.loads(re.get('https://www.irctc.co.in/nget/assets/json/labels_en.json').content)
        #json station data
        headers={
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'greq': tt(),
            'bmirak': 'webbm',
            'Content-Language': 'en',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://www.irctc.co.in/nget/',
            'Cookie': cook,
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }
        (json.loads(re.get('https://www.irctc.co.in/eticketing/protected/mapps1/stationData',headers=headers).content))

        #train list
        ((re.get('https://www.irctc.co.in/eticketing/trainList',headers=headers).content))
        #profile id related
        cook=headers['Cookie']
        data=((re.get(f'https://www.irctc.co.in/eticketing/protected/profile/textToNumber/{tt()}',headers=headers).headers))
        jsessionId=data['Set-Cookie'][0:data['Set-Cookie'].find(";")]
        pre=data['Set-Cookie'][data['Set-Cookie'].find(","):]
        et_appVIP1=pre[1:pre.find(";")]
        cook=cook[0:cook.find(";")]+f"; {jsessionId}; {et_appVIP1}"
        print(cook)
        headers['Cookie']=cook
        ((re.get(f'https://www.irctc.co.in/eticketing/protected/profile/textToNumber/{tt()}',headers=headers).content))
        ((re.get(f'https://api.unibots.in/block?client=Irctc&page=www.irctc.co.in/nget/train-search').content))
        headers['Cookie']=headers['Cookie']+f'; _ga_SHTZYKNHG2=GS1.1.{1687195671}.2.1.{1687195674}.0.0.0; _ga=GA1.1.1904534327.{1687187680}; _ga_5BYVGN5H5L=GS1.1.{1687195671}.2.0.{1687195671}.0.0.0; _ga_7K0RMWL72E=GS1.1.{1687195679}.1.0.{1687195679}.0.0.0'
        payloads={"concessionBooking":'false',"srcStn":"NDLS","destStn":"LKO","jrnyClass":"","jrnyDate":"20230619","quotaCode":"GN","currentBooking":"false","flexiFlag":'false',"handicapFlag":'false',"ticketType":"E","loyaltyRedemptionBooking":'false',"ftBooking":'false'}
        print(re.post("https://www.irctc.co.in/eticketing/protected/mapps1/altAvlEnq/TC",headers=headers,data=payloads).content)
        print(tt())
        #1687237774902
        #1687195674
Test_Builds.builds()