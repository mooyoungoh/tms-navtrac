from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import pandas as pd
from bs4 import BeautifulSoup

import time
import datetime

from model.tms_entity import TMS

def isNaN(num):
    return num != num

########################### DATE ############ TIME ZONE ###########

def getDate(): 

    today = datetime.date.today()

    yesterday = datetime.datetime(
        year=today.year,
        month=today.month,
        day=today.day
    ) + datetime.timedelta(days=-1)

    yesterday = yesterday.strftime('%m%d')

    return yesterday   

#######################################################################

# initialize the Chrome driver
def browerDriver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])   
    options.add_experimental_option("detach", True)                                                 # Leave the browser open
    #driver = webdriver.Chrome("./chromedriver.exe", options=options)                               # deprecated
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    return driver

#url
url = 'http://ngl.logisticsmax.com/'

#login info
id = "mooyoung.o"
pw = "moo6093"

def main():
    driver = browerDriver()
    # driver.maximize_window()
    driver.get(url)

    username = driver.find_element(By.NAME, 'uid')  #find by name
    password = driver.find_element(By.NAME, 'pwd')  #find by password

    username.send_keys(id)                          #fill the id
    password.send_keys(pw)                          #fill the password

    driver.find_element(By.NAME, 'button1').click() #login page
    driver.find_element(By.ID, 'T3').click()        #Daily In/Out Page

    time.sleep(1)
    ######################################################################################################


    ####################Frame switch######################## IMPORTATNT####################################

    iframe = driver.find_element(By.NAME, 'cf_main_sub')
    driver.switch_to.frame(iframe)

    #######################################################################################################

    location = driver.find_element(By.NAME, 'yard_location')
    location.send_keys('PHOENIX')
    time.sleep(1)

    state_date = driver.find_element(By.NAME, 'start_date')
    state_date.clear()
    time.sleep(1)
    state_date.send_keys(getDate())

    end_date = driver.find_element(By.NAME, 'end_date')
    end_date.clear()
    time.sleep(1)
    end_date.send_keys(getDate())

    driver.find_element(By.ID, 'button2').click()   ## Search Button
    time.sleep(1)
    #########################################################################################################################

    html=driver.page_source

    soup=BeautifulSoup(html,'html.parser')

    div=soup.select_one("div#table-container") # table 

    table=pd.read_html(str(div))[0]

    dict = {}

    for index, row in table.iterrows():
        
        if index == 0 or index == len(table)-1:
            continue

        index = -1
        no = -1
        site = ''
        port = ''
        type = ''
        containerNum = ''
        size = ''
        chasisNum = ''
        pool = ''
        plate = ''
        seal = ''
        createdAt = ''
        dmg = ''
        truckNum =''
        driverName =''
        user =''
        tires = ''
        tier =''
        remark =''
        repaired =''
        
        if row[0] != None and isNaN(row[0]) == False :
            no = row[0]
        if row[1] != None and isNaN(row[1]) == False :
            site = row[1]
        if row[2] != None and isNaN(row[2]) == False :        
            port = row[2]
        if row[3] != None and isNaN(row[3]) == False :
            type = row[3]
        if row[4] != None and isNaN(row[4]) == False :
            containerNum = row[4]
        if row[5] != None and isNaN(row[5]) == False :
            size = row[5]
        if row[6] != None and isNaN(row[6]) == False :
            chasisNum = row[6]
        if row[7] != None and isNaN(row[7]) == False :
            pool = row[7]
        if row[8] != None and isNaN(row[8]) == False :
            plate = row[8]
        if row[9] != None and isNaN(row[9]) == False :
            seal = row[9]
        if row[10] != None and isNaN(row[10]) == False :
            createdAt = row[10]
        if row[11] != None and isNaN(row[11]) == False :
            dmg = row[11]
        if row[12] != None and isNaN(row[12]) == False :
            truckNum = row[12]
        if row[13] != None and isNaN(row[13]) == False :
            driverName = row[13]
        if row[14] != None and isNaN(row[14]) == False :
            user = row[14]
        if row[15] != None and isNaN(row[15]) == False :
            tires = row[15]
        if row[16] != None and isNaN(row[16]) == False :
            tier = row[16]
        if row[17] != None and isNaN(row[17]) == False :
            remark = row[17]
        if row[18] != None and isNaN(row[18]) == False :
            repaired = row[18]

        key = str(containerNum)
        obj = object()
        
        if key in dict:
            tmp = dict.get(key)[-1]
            total = tmp.total + 1
            obj = TMS(total, no, site, port, type, containerNum, size, chasisNum, pool, plate, seal, createdAt, dmg, truckNum, driverName, user, tires, tier, remark, repaired)    
            dict[key].append(obj)
            
        else:        
            dict[key] = []
            obj = TMS(1, no, site, port, type, containerNum, size, chasisNum, pool, plate, seal, createdAt, dmg, truckNum, driverName, user, tires, tier, remark, repaired)
            dict[key].append(obj)
    

    return dict



main()