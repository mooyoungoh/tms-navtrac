from threading import get_ident
import requests
import datetime

import pytz
import time
import delorean
from model.navTrac_entity import NavTrack

################# url ###########################################
authUrl = "https://api.navtrac.com/auth"
searchUrl = "https://api.navtrac.com/observations/search"

#################################################################

##################### login info ################################

password = "12345678"
email = "ngl@navtrac.com"
loginType = "user"

#################################################################
############# Header ############################################

def header(token):
    headers = {
        'Authorization': token
    }    
    return headers

##################################################################
############# Date ###############################################

def dateModify(param):
    tmp = param.split('T')
    dt = datetime.datetime.strptime(tmp[0], '%Y-%m-%d')
    tmp1 = str(dt.month).zfill(2)
    tmp2 = str(dt.day)
    tmp3 = str(dt.year)
    return tmp1+tmp2+tmp3

##################################################################
######################### PayLoad ################################

payload = {
    "data": {
        "password": password,
        "username": email,
        "type": loginType
    }
}

###################################################################
########################### DATE ############ TIME ZONE ###########

def localToUtc(time):
    dl = delorean.Delorean(time, timezone='America/Phoenix').shift('UTC').datetime
    return dl

def localToUtc2(time, timeZone):
    dl = delorean.Delorean(time, timezone=timeZone).shift('UTC').datetime
    return dl


today = datetime.date.today()

beginYesterday = datetime.datetime(
    year=today.year,
    month=today.month,
    day=today.day
) + datetime.timedelta(days=-1)

endYesterday = datetime.datetime(
    year=today.year,
    month=today.month,
    day=today.day
) + datetime.timedelta(microseconds=-1)

beginYesterday = localToUtc(beginYesterday)
endYesterday = localToUtc(endYesterday)

beginYesterday = beginYesterday.strftime('%Y-%m-%dT%H:%M:%SZ')
endYesterday = endYesterday.strftime('%Y-%m-%dT%H:%M:%SZ')

print(beginYesterday)
print(endYesterday)

#######################################################################

## Hard Coding Version ##
payloadSearch = {
    "data": {
        "page": {"number": "0", "size": "200"},
        "filter": {
            "gateId": "017916e6-54c7-2b91-0d55-17ac51c37f00",
            "createdAt": {
                "$between": [
                    #beginYesterday,
                    #endYesterday
                    '2022-08-09T07:00:00Z',
                    '2022-08-10T06:59:59Z'
                ]
            }
        },
        "sort": "id DESC"
    }         
}

######################################################################################

def buildSearch(location, searchTitle, searchContent, searchDate, sort):
    # location - array
    # searchDate - array
    # searchTitle - string
    # searchContent - string
    # sort - string 

    data = {}
    data['filter'] = {}
    
    if(location != "" or len(location) !=0):
        data['filter']['gateId'] = location 
    if(searchTitle != "" or len(searchTitle) !=0):
        data['filter'][searchTitle] = searchContent
    if(searchDate != "" or len(searchDate) !=0):
        data['filter']['detectedAt'] = {}
        data['filter']['detectedAt']['$between'] = searchDate
    if(sort != "" or len(sort) !=0):
        data['sort'] = sort

    print(data)

#### TEST ####

# buildSearch("la","tt","qww","321","desc")

#########################################################################################
def main():

    try:
        response = requests.post(url=authUrl, json=payload)

        jsonReponse = response.json()

        # print(jsonReponse['data']['token'])
        token = "JWT "

        token += jsonReponse['data']['token']

        #print(token)

        responseContent = requests.post(url=searchUrl, json=payloadSearch, headers=header(token))

        #print(responseContent.text)

        responseContent = responseContent.json()

        ## init model object
        
        load = []
        vehicle =[]
        chassis = []

        dict = {}

        tt = 0

        for i in responseContent['data']:
            tt += 1
            direction = ''
            createdAt = ''
            detectedAt = ''
            updatedAt = ''
            hasSeal = ''
            gateId = ''
            sealNumber = ''
            hasReeferUnit = ''
            vehicle = ''
            imagePaths = ''

            if 'direction' in i:
                direction = i.get('direction')
            if 'createdAt' in i:
                createdAt = i.get('createdAt')
            if 'detectedAt' in i:
                detectedAt = i.get('detectedAt')
            if 'updatedAt' in i:
                updatedAt = i.get('updatedAt')
            if 'hasSeal' in i:
                hasSeal = i.get('hasSeal')
            if 'gateId' in i:
                gateId = i.get('gateId')
            if 'sealNumber' in i:
                sealNumber = i.get('sealNumber')
            if 'hasReeferUnit' in i:
                hasReeferUnit = i.get('hasReeferUnit')
            if 'vehicle' in i:
                vehicle = (i.get('vehicle'))
            if 'imagePaths' in i:
                imagePaths = (i.get('imagePaths'))

            ### meta ####
            meta= (i.get('meta'))
            if 'loadNumber' in meta:
                loadId = meta['loadNumber']
            if 'assetChassis' in meta:
                chassisId = meta['assetChassis']

            #print(tmpObj)
            key = ''
            if loadId is not None:
                key1 = str(loadId)
                
            obj = object()

            if key in dict:
                tmp = dict.get(key)[-1]
                total = tmp.total + 1
                obj = NavTrack(total, direction, createdAt, detectedAt, updatedAt, hasSeal, loadId, gateId, sealNumber, hasReeferUnit, load, vehicle, chassis, imagePaths)
                dict[key].append(obj)
                
            else:
                dict[key] = []
                obj = NavTrack(1, direction, createdAt, detectedAt, updatedAt, hasSeal, loadId, gateId, sealNumber, hasReeferUnit, load, vehicle, chassis, imagePaths)
                dict[key].append(obj)
                
            date = dateModify(createdAt)
        print(tt)
        return dict

    except NameError:
        print(NameError)

main()

###########################################################################