import unittest
import time
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from multiprocessing.connection import wait
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from XTestRunner import HTMLTestRunner
from XTestRunner import XMLTestRunner
from XTestRunner import SMTP

class Test2(unittest.TestCase):
    """前站體育測試"""
    def test_SABA(self):
        """SABA測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
#        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
        self.driver.delete_all_cookies()
        self.base_url = "https://stg-t1.rpgp.cc/"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        element=WebDriverWait(self.driver,120,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[4]/div[2]/div[1]/span')
        login.click()           
        element=self.driver.find_element(By.ID,'username')
        element.send_keys('qatest1')
        element.send_keys('\ue004')
        element =self.driver.find_element(By.ID,'password')
        element.send_keys('aA19890610')   
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[5]/div[3]/span").click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)          
        #SABA體育   
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[1]/div[2]').click()     
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/iframe'))
        # 2022.12.09新增api status 判斷
        headers = {'content-type':'application/json; charset=utf-8'}
        r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
        token = r.json()['token']
        r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
        print (r.status_code)
        self.assertEqual(r.status_code, 200)
        #
        time.sleep(40)
        tilt =self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]").get_attribute('innerHTML')
        self.images.append(self.driver.get_screenshot_as_base64())
        self.assertNotEqual(tilt, "Prohibited Visit")         
        self.driver.switch_to.default_content()
        tilt =self.driver.title
        print(tilt)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[3]/div/div').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="simple-menu"]/div[3]/ul/li[1]').click()
        self.images.append(self.driver.get_screenshot_as_base64())
        element=WebDriverWait(self.driver,120,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )
            #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
            #優惠彈窗   
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)           
            #SABA體育
            self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[1]/div[2]').click()   
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div/iframe'))
            # 2022.12.09新增api status 判斷
            headers = {'content-type':'application/json; charset=utf-8'}
            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
            token = r.json()['token']
            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
            print (r.status_code)
            self.assertEqual(r.status_code, 200)
            #            
            time.sleep(40)
            tilt =self.driver.title
            tilt =self.driver.find_element(By.XPATH,"/html/head/title").get_attribute('textContent')
            print(tilt)
            self.images.append(self.driver.get_screenshot_as_base64())
            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")
            self.driver.close()
        
    def test_mosaba(self):
        """手機saba測試"""
        self.chrome_options = Options()
#        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.delete_all_cookies()      
        self.driver.get('https://stg-t1.rpgp.cc/')
        element=WebDriverWait(self.driver,30,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
        )
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        #優惠彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header[1]/div/div[1]/div/div[2]/div/div[1]')
        login.click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/div/input").send_keys("qatest1")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[4]/div[1]/input").send_keys("aA19890610")
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.find_element(By.NAME, "登录").click()
        time.sleep(3)        
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[1]').click()  
        time.sleep(3)
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameType1"]').click()  
        time.sleep(3)
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                # 2022.12.09新增api status 判斷
                headers = {'content-type':'application/json; charset=utf-8'}
                r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                token = r.json()['token']
                r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                print (r.status_code)
                self.assertEqual(r.status_code, 200)
                #
                time.sleep(40)
                tilt =self.driver.title
                print(tilt)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.assertNotEqual(tilt, "PGG - 专业娱乐平台")  
                self.driver.switch_to.default_content()
                self.driver.switch_to.window(handles[0])
                tilt =self.driver.title
                print(tilt)
                self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/button[5]/span[1]/div').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[1]/div/div[10]/div/div[1]').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="checkbox-list-label-en-US"]/span').click()
                self.driver.find_element(By.XPATH,' //*[@id="root"]/div[2]/div[2]/div').click()                   
                element=WebDriverWait(self.driver,30,1).until(
                #條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
                )
                    #公告彈窗
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():                       
                    self.images.append(self.driver.get_screenshot_as_base64())
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                        
                    time.sleep(3)
                     #優惠彈窗   
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[3]").is_displayed():
                    self.images.append(self.driver.get_screenshot_as_base64())                        
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                    
                    time.sleep(3)           
                    #saba體育
                    handle = self.driver.current_window_handle   
                    self.driver.find_element(By.XPATH, '//*[@id="gameType1"]').click()  
                    time.sleep(3)
                    handles = self.driver.window_handles
                    for newhandle in handles:
                        # 開啟新的視窗
                        if newhandle!=handle:
                            self.driver.switch_to.window(newhandle)
                            # 2022.12.09新增api status 判斷
                            headers = {'content-type':'application/json; charset=utf-8'}
                            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                            token = r.json()['token']
                            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                            print (r.status_code)
                            self.assertEqual(r.status_code, 200)
                            #
                            time.sleep(40)
                            tilt =self.driver.title
                            print(tilt)
                            self.images.append(self.driver.get_screenshot_as_base64())
                            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")            
                            self.driver.switch_to.default_content()                    
                            self.driver.quit()           
        
    def test_Betconstruct(self):
        """Betconstruct測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
#        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
        self.driver.delete_all_cookies()      
        self.base_url = "https://stg-t1.rpgp.cc/"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        element=WebDriverWait(self.driver,30,1).until(
#        條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[4]/div[2]/div[1]/span')
        login.click()           
        element=self.driver.find_element(By.ID,'username')
        element.send_keys('qatest1')
        element.send_keys('\ue004')
        element =self.driver.find_element(By.ID,'password')
        element.send_keys('aA19890610')   
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[5]/div[3]/span").click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)          
        #Betconstruct體育   
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[2]/div[2]').click()     
        time.sleep(3)
        # 2022.12.09新增api status 判斷
        headers = {'content-type':'application/json; charset=utf-8'}
        r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
        token = r.json()['token']
        r= requests.get('https://stg-t1.rpgp.cc/api/game/bc',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
        print (r.status_code)
        self.assertEqual(r.status_code, 200)
        #
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/iframe'))
        time.sleep(30)
        tilt =self.driver.find_element(By.XPATH,"/html/head/title").get_attribute('textContent')
        print(tilt)
        self.images.append(self.driver.get_screenshot_as_base64())
        self.assertNotEqual(tilt, "PGG - 专业娱乐平台")
        self.driver.switch_to.default_content()
        tilt =self.driver.title
        print(tilt)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[3]/div/div').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="simple-menu"]/div[3]/ul/li[1]').click()
        element=WebDriverWait(self.driver,30,1).until(
#        條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )
            #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
            #優惠彈窗   
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)           
            #Betconstruct體育
            self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[2]/div[2]').click()   
            time.sleep(3)
            # 2022.12.09新增api status 判斷
            headers = {'content-type':'application/json; charset=utf-8'}
            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
            token = r.json()['token']
            r= requests.get('https://stg-t1.rpgp.cc/api/game/bc',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
            print (r.status_code)
            self.assertEqual(r.status_code, 200)
            #
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div/iframe'))
            time.sleep(40)
            tilt =self.driver.title
            tilt =self.driver.find_element(By.XPATH,"/html/head/title").get_attribute('textContent')
            print(tilt)
            self.images.append(self.driver.get_screenshot_as_base64())
            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")
            self.driver.close()        

    def test_moBetconstruct(self):
        """手機Betconstruct測試(僅使用api測試)"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.delete_all_cookies()  
        self.driver.get('https://stg-t1.rpgp.cc/')
        element=WebDriverWait(self.driver,30,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
        )
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        #優惠彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header[1]/div/div[1]/div/div[2]/div/div[1]')
        login.click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/div/input").send_keys("qatest1")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[4]/div[1]/input").send_keys("aA19890610")
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.find_element(By.NAME, "登录").click()
        time.sleep(3)        
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[1]').click()  
        time.sleep(3)
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdBC1"]').click()  
        time.sleep(3) 
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if handle!=newhandle:           
                time.sleep(5)
                # 2022.12.09新增api status 判斷
                headers = {'content-type':'application/json; charset=utf-8'}
                r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                token = r.json()['token']
                r= requests.get('https://stg-t1.rpgp.cc/api/game/bc',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                print (r.status_code)
                self.assertEqual(r.status_code, 200)
                #
                self.driver.switch_to.window(handles[0])
                self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/button[5]/span[1]/div').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[1]/div/div[10]/div/div[1]').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="checkbox-list-label-en-US"]/span').click()
                self.driver.find_element(By.XPATH,' //*[@id="root"]/div[2]/div[2]/div').click()                   
                time.sleep(3)
                    #公告彈窗
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():                       
                    self.images.append(self.driver.get_screenshot_as_base64())
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                        
                    time.sleep(3)
                     #優惠彈窗   
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[3]").is_displayed():
                    self.images.append(self.driver.get_screenshot_as_base64())                        
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                    
                    time.sleep(3)           
                    #Betconstruct體育
                    handle = self.driver.current_window_handle   
                    self.driver.find_element(By.XPATH, '//*[@id="gameIdBC1"]').click()  
                    time.sleep(3)
                    handles = self.driver.window_handles
                    for newhandle in handles:
                        # 開啟新的視窗
                        if newhandle!=handle:
                            self.driver.switch_to.window(newhandle)
                            time.sleep(5)
                            # 2022.12.09新增api status 判斷
                            headers = {'content-type':'application/json; charset=utf-8'}
                            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                            token = r.json()['token']
                            r= requests.get('https://stg-t1.rpgp.cc/api/game/bc',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                            print (r.status_code)
                            self.assertEqual(r.status_code, 200)
                            #                           
                            self.driver.quit()

    def test_sbobet(self):
        """sbobet測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
#        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
        self.driver.delete_all_cookies()
        self.base_url = "https://stg-t1.rpgp.cc/"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        element=WebDriverWait(self.driver,60,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[4]/div[2]/div[1]/span')
        login.click()           
        element=self.driver.find_element(By.ID,'username')
        element.send_keys('qatest1')
        element.send_keys('\ue004')
        element =self.driver.find_element(By.ID,'password')
        element.send_keys('aA19890610')   
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[5]/div[3]/span").click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)          
        #sbobet體育   
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        target = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div[2]/div/div[2]/div[2]')
        self.driver.execute_script("arguments[0].scrollIntoView();",target)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[2]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/iframe'))
        # 2022.12.09新增api status 判斷
        headers = {'content-type':'application/json; charset=utf-8'}
        r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
        token = r.json()['token']
        r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
        print (r.status_code)
        self.assertEqual(r.status_code, 200)
        #
        time.sleep(40)
        tilt =self.driver.find_element(By.XPATH,"/html/head/title").get_attribute('textContent')
        print(tilt)
        self.images.append(self.driver.get_screenshot_as_base64())
        self.assertNotEqual(tilt, "PGG - 专业娱乐平台")
        self.driver.switch_to.default_content()
        tilt =self.driver.title
        print(tilt)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[3]/div/div').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="simple-menu"]/div[3]/ul/li[1]').click()
        self.images.append(self.driver.get_screenshot_as_base64())
        element=WebDriverWait(self.driver,60,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )
            #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
            #優惠彈窗   
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)           
            ##sbobet體育
            self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
            target = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div[2]/div/div[2]/div[2]')
            self.driver.execute_script("arguments[0].scrollIntoView();",target)
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[2]/div[2]').click()  
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div/iframe'))
            # 2022.12.09新增api status 判斷
            headers = {'content-type':'application/json; charset=utf-8'}
            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
            token = r.json()['token']
            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
            print (r.status_code)
            self.assertEqual(r.status_code, 200)
            #
            time.sleep(40)
            tilt =self.driver.title
            tilt =self.driver.find_element(By.XPATH,"/html/head/title").get_attribute('textContent')
            print(tilt)
            self.images.append(self.driver.get_screenshot_as_base64())
            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")
            self.driver.close()

    def test_mosbobet(self):
        """手機sbobet測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        element=WebDriverWait(self.driver,60,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
        )
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        #優惠彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header[1]/div/div[1]/div/div[2]/div/div[1]')
        login.click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/div/input").send_keys("qatest1")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[4]/div[1]/input").send_keys("aA19890610")
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.find_element(By.NAME, "登录").click()
        time.sleep(3)        
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[1]').click()  
        time.sleep(3)
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdSBOTF1"]').click()  
        time.sleep(3)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                # 2022.12.09新增api status 判斷
                headers = {'content-type':'application/json; charset=utf-8'}
                r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                token = r.json()['token']
                r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                print (r.status_code)
                self.assertEqual(r.status_code, 200)
                #
                time.sleep(40)                         
                tilt =self.driver.title
                print(tilt)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.assertNotEqual(tilt, "PGG - 专业娱乐平台")              
                self.driver.switch_to.default_content()                    
                self.driver.switch_to.window(handles[0])
                tilt =self.driver.title
                print(tilt)
                self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/button[5]/span[1]/div').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[1]/div/div[10]/div/div[1]').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="checkbox-list-label-en-US"]/span').click()
                self.driver.find_element(By.XPATH,' //*[@id="root"]/div[2]/div[2]/div').click()                                  
                element=WebDriverWait(self.driver,60,1).until(
                #條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
                )
                    #公告彈窗
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():                       
                    self.images.append(self.driver.get_screenshot_as_base64())
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                        
                    time.sleep(3)
                     #優惠彈窗   
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[3]").is_displayed():
                    self.images.append(self.driver.get_screenshot_as_base64())                        
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                    
                    time.sleep(3)           
                    #mosbobet
                    handle = self.driver.current_window_handle   
                    self.driver.find_element(By.XPATH, '//*[@id="gameIdSBOTF1"]').click()  
                    time.sleep(3)
                    handles = self.driver.window_handles
                    for newhandle in handles:
                        # 開啟新的視窗
                        if newhandle!=handle:
                            self.driver.switch_to.window(newhandle)
                            # 2022.12.09新增api status 判斷
                            headers = {'content-type':'application/json; charset=utf-8'}
                            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                            token = r.json()['token']
                            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                            print (r.status_code)
                            self.assertEqual(r.status_code, 200)
                            #
                            time.sleep(40)
                            tilt =self.driver.title
                            print(tilt)
                            self.images.append(self.driver.get_screenshot_as_base64())
                            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")           
                            self.driver.switch_to.default_content()                    
                            self.driver.quit()

    def test_wgvia(self):
        """wgvia測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
        self.driver.delete_all_cookies()
        self.base_url = "https://stg-t1.rpgp.cc/"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        element=WebDriverWait(self.driver,60,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
        #優惠彈窗   
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3) 
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[4]/div[2]/div[1]/span')
        login.click()           
        element=self.driver.find_element(By.ID,'username')
        element.send_keys('qatest1')
        element.send_keys('\ue004')
        element =self.driver.find_element(By.ID,'password')
        element.send_keys('aA19890610')   
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[5]/div[3]/span").click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)          
            #wgvia體育
        handle = self.driver.current_window_handle   
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[3]/div[2]').click()   
        handles = self.driver.window_handles
        for newhandle in handles:
                # 開啟新的視窗
                if newhandle!=handle:
                    self.driver.switch_to.window(newhandle)
                    time.sleep(3)
                     # 2022.12.09新增api status 判斷
                    headers = {'content-type':'application/json; charset=utf-8'}
                    r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                    token = r.json()['token']
                    r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                    print (r.status_code)
                    self.assertEqual(r.status_code, 200)
                    #
                    time.sleep(30)
                    self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="mainBody"]/iframe'))
                    tilt =self.driver.title
                    print(tilt)
                    self.images.append(self.driver.get_screenshot_as_base64())
                    self.assertNotEqual(tilt, "PGG - 专业娱乐平台")              
                    self.driver.switch_to.default_content()
                    self.driver.switch_to.window(handles[0])
                    tilt =self.driver.title
                    print(tilt)
                    self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[3]/div/div').click()
                    time.sleep(3)
                    self.driver.find_element(By.XPATH, '//*[@id="simple-menu"]/div[3]/ul/li[1]').click()
                    element=WebDriverWait(self.driver,60,1).until(
                    #條件：直到元素載入完成
                    EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
                    )
                     #公告彈窗
                    if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
                        self.images.append(self.driver.get_screenshot_as_base64())
                        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
                        time.sleep(3)
                     #優惠彈窗   
                    if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
                        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
                        self.images.append(self.driver.get_screenshot_as_base64())
                        time.sleep(3)           
                    #wgvia體育
                    handle = self.driver.current_window_handle   
                    self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
                    self.images.append(self.driver.get_screenshot_as_base64())
                    time.sleep(3)
                    self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[3]/div[2]').click()   
                    time.sleep(30)
                    handles = self.driver.window_handles
                    for newhandle in handles:
                        # 開啟新的視窗
                            if newhandle!=handle:
                                self.driver.switch_to.window(newhandle)
                                time.sleep(3)
                                # 2022.12.09新增api status 判斷
                                headers = {'content-type':'application/json; charset=utf-8'}
                                r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                                token = r.json()['token']
                                r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                                print (r.status_code)
                                self.assertEqual(r.status_code, 200)
                                #
                                time.sleep(40)
                                self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="mainBody"]/iframe'))
                                tilt =self.driver.title
                                print(tilt)
                                self.images.append(self.driver.get_screenshot_as_base64())
                                self.assertNotEqual(tilt, "PGG - 专业娱乐平台")              
                                self.driver.switch_to.default_content()                    
                                self.driver.quit()
                                
    def test_mowgvia(self):
        """手機wgvia測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.delete_all_cookies()
        self.driver.get('https://stg-t1.rpgp.cc/')
        element=WebDriverWait(self.driver,30,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
        )
            #以下彈窗請依照設定進行執行或非執行
            #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
            #優惠彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header[1]/div/div[1]/div/div[2]/div/div[1]')
        login.click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/div/input").send_keys("qatest1")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[4]/div[1]/input").send_keys("aA19890610")
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.find_element(By.NAME, "登录").click()
        time.sleep(3)        
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[1]').click()  
        time.sleep(3)
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdWGVIA1"]').click()  
        time.sleep(3)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
                # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                time.sleep(3)
                # 2022.12.09新增api status 判斷
                headers = {'content-type':'application/json; charset=utf-8'}
                r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                token = r.json()['token']
                r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                print (r.status_code)
                self.assertEqual(r.status_code, 200)
                #
                time.sleep(30)
                tilt =self.driver.title
                self.images.append(self.driver.get_screenshot_as_base64())
                self.assertNotEqual(tilt, "PGG - 专业娱乐平台")  
                self.driver.switch_to.default_content()
                self.driver.switch_to.window(handles[0])
                tilt =self.driver.title
                print(tilt)
                self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/button[5]/span[1]/div').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[1]/div/div[10]/div/div[1]').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="checkbox-list-label-en-US"]/span').click()
                self.driver.find_element(By.XPATH,' //*[@id="root"]/div[2]/div[2]/div').click()                   
                element=WebDriverWait(self.driver,60,1).until(
                #條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
                )
                    #公告彈窗
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():                       
                    self.images.append(self.driver.get_screenshot_as_base64())
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                        
                    time.sleep(3)
                     #優惠彈窗   
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[3]").is_displayed():
                    self.images.append(self.driver.get_screenshot_as_base64())                        
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                    
                    time.sleep(3)           
                    #wgvia體育
                    handle = self.driver.current_window_handle   
                    self.driver.find_element(By.XPATH, '//*[@id="gameIdWGVIA1"]').click()  
                    time.sleep(3)
                    handles = self.driver.window_handles
                    for newhandle in handles:
                        # 開啟新的視窗
                        if newhandle!=handle:
                            self.driver.switch_to.window(newhandle)
                            # 2022.12.09新增api status 判斷
                            headers = {'content-type':'application/json; charset=utf-8'}
                            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                            token = r.json()['token']
                            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                            print (r.status_code)
                            self.assertEqual(r.status_code, 200)
                            #
                            time.sleep(30)
                            self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="mainBody"]/iframe'))
                            tilt =self.driver.title
                            print(tilt)
                            self.images.append(self.driver.get_screenshot_as_base64())
                            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")              
                            self.driver.switch_to.default_content()                    
                            self.driver.quit()

    def test_AWC_COCKFIGH(self):
        """AWC_COCKFIGH測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
        self.driver.delete_all_cookies()
        self.base_url = "https://stg-t1.rpgp.cc/"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        element=WebDriverWait(self.driver,30,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )        
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
        #優惠彈窗 
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[4]/div[2]/div[1]/span')
        login.click()           
        element=self.driver.find_element(By.ID,'username')
        element.send_keys('qatest1')
        element.send_keys('\ue004')
        element =self.driver.find_element(By.ID,'password')
        element.send_keys('aA19890610')   
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[5]/div[3]/span").click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)          
        #AWC_COCKFIGH體育  
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[4]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        # 2022.12.09新增api status 判斷
        headers = {'content-type':'application/json; charset=utf-8'}
        r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
        token = r.json()['token']
        r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
        print (r.status_code)
        self.assertEqual(r.status_code, 200)
        #
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div/iframe'))
        time.sleep(40)
        tilt =self.driver.find_element(By.XPATH,"/html/head/title").get_attribute('textContent')
        print(tilt)
        self.images.append(self.driver.get_screenshot_as_base64())
        self.assertNotEqual(tilt, "PGG - 专业娱乐平台")
        self.images.append(self.driver.get_screenshot_as_base64())        
        self.driver.switch_to.default_content()
        tilt =self.driver.title
        print(tilt)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[3]/div/div').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="simple-menu"]/div[3]/ul/li[1]').click()
        self.images.append(self.driver.get_screenshot_as_base64())
        element=WebDriverWait(self.driver,30,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )            
            #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
            #優惠彈窗   
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)           
            #AWC_COCKFIGH體育 
            self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[4]/div[2]').click()   
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
            # 2022.12.09新增api status 判斷
            headers = {'content-type':'application/json; charset=utf-8'}
            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
            token = r.json()['token']
            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
            print (r.status_code)
            self.assertEqual(r.status_code, 200)
            #
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div/iframe'))
            time.sleep(40)
            tilt =self.driver.title
            tilt =self.driver.find_element(By.XPATH,"/html/head/title").get_attribute('textContent')
            print(tilt)
            self.images.append(self.driver.get_screenshot_as_base64())
            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")
            self.driver.close()
            
    def test_moAWC_COCKFIGH(self):
        """手機AWC_COCKFIGH測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        element=WebDriverWait(self.driver,30,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
        )
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        #優惠彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header[1]/div/div[1]/div/div[2]/div/div[1]')
        login.click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/div/input").send_keys("qatest1")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[4]/div[1]/input").send_keys("aA19890610")
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.find_element(By.NAME, "登录").click()
        time.sleep(3)        
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[1]').click()  
        time.sleep(3)
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdAWC_COCKFIGHT1"]').click()  
        time.sleep(3)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                # 2022.12.09新增api status 判斷
                headers = {'content-type':'application/json; charset=utf-8'}
                r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                token = r.json()['token']
                r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                print (r.status_code)
                self.assertEqual(r.status_code, 200)
                #
                time.sleep(30)
                self.images.append(self.driver.get_screenshot_as_base64())
                tilt =self.driver.title
                print(tilt)
                self.assertNotEqual(tilt, "PGG - 专业娱乐平台")              
                self.driver.switch_to.default_content()
                self.driver.switch_to.window(handles[0])
                self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/button[5]/span[1]/div').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[1]/div/div[10]/div/div[1]').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="checkbox-list-label-en-US"]/span').click()
                self.driver.find_element(By.XPATH,' //*[@id="root"]/div[2]/div[2]/div').click()                   
                element=WebDriverWait(self.driver,30,1).until(
                #條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
                )
                    #公告彈窗
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():                       
                    self.images.append(self.driver.get_screenshot_as_base64())
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                        
                    time.sleep(3)
                     #優惠彈窗   
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[3]").is_displayed():
                    self.images.append(self.driver.get_screenshot_as_base64())                        
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                    
                    time.sleep(3)           
                    #AWC_COCKFIGHT
                    handle = self.driver.current_window_handle   
                    self.driver.find_element(By.XPATH, '//*[@id="gameIdAWC_COCKFIGHT1"]').click()  
                    time.sleep(3)
                    handles = self.driver.window_handles
                    for newhandle in handles:
                        # 開啟新的視窗
                        if newhandle!=handle:
                            self.driver.switch_to.window(newhandle)
                            # 2022.12.09新增api status 判斷
                            headers = {'content-type':'application/json; charset=utf-8'}
                            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                            token = r.json()['token']
                            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                            print (r.status_code)
                            self.assertEqual(r.status_code, 200)
                            #
                            time.sleep(30)
                            tilt =self.driver.title
                            print(tilt)
                            self.images.append(self.driver.get_screenshot_as_base64())
                            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")              
                            self.driver.switch_to.default_content()                    
                            self.driver.quit() 

    def test_AWC_RCB(self):
        """AWC_RCB測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
#        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
        self.driver.delete_all_cookies()
        self.base_url = "https://stg-t1.rpgp.cc/"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        element=WebDriverWait(self.driver,60,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )        
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
        #優惠彈窗 
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[4]/div[2]/div[1]/span')
        login.click()           
        element=self.driver.find_element(By.ID,'username')
        element.send_keys('qatest1')
        element.send_keys('\ue004')
        element =self.driver.find_element(By.ID,'password')
        element.send_keys('aA19890610')   
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[5]/div[3]/span").click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)          
        #AWC_RCB體育  
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[1]/div[2]').click()     
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div/iframe'))
        headers = {'content-type':'application/json; charset=utf-8'}
        # 2022.12.09新增api status 判斷
        r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
        token = r.json()['token']
        r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
        print (r.status_code)
        self.assertEqual(r.status_code, 200)
        #
        time.sleep(40)
        tilt =self.driver.find_element(By.XPATH,"/html/head/title").get_attribute('textContent')
        print(tilt)
        self.images.append(self.driver.get_screenshot_as_base64())
        self.assertNotEqual(tilt, "PGG - 专业娱乐平台")   
        self.driver.switch_to.parent_frame()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[3]/div/div').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="simple-menu"]/div[3]/ul/li[1]').click()
        self.images.append(self.driver.get_screenshot_as_base64())
        element=WebDriverWait(self.driver,60,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        ) 
            #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
            #優惠彈窗   
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)           
            ##AWC_RCB體育
            self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[1]/div[2]').click()   
            time.sleep(40)
            # 2022.12.09新增api status 判斷
            headers = {'content-type':'application/json; charset=utf-8'}
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div/iframe'))
            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
            token = r.json()['token']
            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
            print (r.status_code)
            self.assertEqual(r.status_code, 200)
            #
            tilt =self.driver.title
            tilt =self.driver.find_element(By.XPATH,"/html/head/title").get_attribute('textContent')
            print(tilt)
            self.images.append(self.driver.get_screenshot_as_base64())
            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")
            self.driver.switch_to.parent_frame()
            self.driver.quit()

    def test_moAWC_RCB(self):
        """手機AWC_RCB測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.delete_all_cookies()
        self.driver.get('https://stg-t1.rpgp.cc/')
        element=WebDriverWait(self.driver,60,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
        )
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        #優惠彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header[1]/div/div[1]/div/div[2]/div/div[1]')
        login.click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/div/input").send_keys("qatest1")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[4]/div[1]/input").send_keys("aA19890610")
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[7]/div[1]').click()
        time.sleep(3)        
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[1]').click()  
        time.sleep(3)
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdAWC_RCB1"]').click()  
        time.sleep(3)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                time.sleep(3)
                # 2022.12.09新增api status 判斷
                headers = {'content-type':'application/json; charset=utf-8'}
                r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                token = r.json()['token']
                r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                print (r.status_code)
                self.assertEqual(r.status_code, 200)
                #
                time.sleep(30)
                tilt =self.driver.title
                print(tilt)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.assertNotEqual(tilt, "PGG - 专业娱乐平台")              
                self.driver.switch_to.default_content()
                self.driver.switch_to.window(handles[0])
                self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/button[5]/span[1]/div').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[1]/div/div[10]/div/div[1]').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="checkbox-list-label-en-US"]/span').click()
                self.driver.find_element(By.XPATH,' //*[@id="root"]/div[2]/div[2]/div').click()                                  
                element=WebDriverWait(self.driver,60,1).until(
                #條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
                )
                    #公告彈窗
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():                       
                    self.images.append(self.driver.get_screenshot_as_base64())
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                        
                    time.sleep(3)
                     #優惠彈窗   
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[3]").is_displayed():
                    self.images.append(self.driver.get_screenshot_as_base64())                        
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                    
                    time.sleep(3)           
                    #AWC_COCKFIGHT
                    handle = self.driver.current_window_handle   
                    self.driver.find_element(By.XPATH, '//*[@id="gameIdAWC_RCB1"]').click()  
                    time.sleep(3)
                    handles = self.driver.window_handles
                    for newhandle in handles:
                        # 開啟新的視窗
                        if newhandle!=handle:
                            self.driver.switch_to.window(newhandle)
                            time.sleep(3)
                            # 2022.12.09新增api status 判斷
                            headers = {'content-type':'application/json; charset=utf-8'}
                            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                            token = r.json()['token']
                            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                            print (r.status_code)
                            self.assertEqual(r.status_code, 200)
                            #
                            time.sleep(30)
                            tilt =self.driver.title
                            print(tilt)
                            self.images.append(self.driver.get_screenshot_as_base64())
                            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")              
                            self.driver.switch_to.default_content()                    
                            self.driver.quit()

    def test_WGFM(self):
        """WGFM測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
#        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
        self.driver.delete_all_cookies()
        self.base_url = "https://stg-t1.rpgp.cc/"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        element=WebDriverWait(self.driver,120,1).until(
#        條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )        
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
#        #優惠彈窗 
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[4]/div[2]/div[1]/span')
        login.click()           
        element=self.driver.find_element(By.ID,'username')
        element.send_keys('qatest1')
        element.send_keys('\ue004')
        element =self.driver.find_element(By.ID,'password')
        element.send_keys('aA19890610')   
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div[5]/div[3]/span').click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)          
        #WGFM體育  
        handle = self.driver.current_window_handle   
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
        wgfm =self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[5]/div[2]')
        self.driver.execute_script("arguments[0].scrollIntoView();", wgfm)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[5]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        handles = self.driver.window_handles
        for newhandle in handles:
            # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                # 2022.12.09新增api status 判斷
                headers = {'content-type':'application/json; charset=utf-8'}
                r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                token = r.json()['token']
                r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                print (r.status_code)
                self.assertEqual(r.status_code, 200)
                #
                time.sleep(40)
                tilt =self.driver.title
                print(tilt)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.assertNotEqual(tilt, "PGG - 专业娱乐平台") 
                self.driver.switch_to.default_content()
                self.driver.switch_to.window(handles[0])
                self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[3]/div/div').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="simple-menu"]/div[3]/ul/li[1]').click()                                
                element=WebDriverWait(self.driver,120,1).until(
                #條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
                )   
                   #公告彈窗
                if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():                       
                    self.images.append(self.driver.get_screenshot_as_base64())
                    self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()                        
                    time.sleep(3)
                     #優惠彈窗   
                if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
                    self.images.append(self.driver.get_screenshot_as_base64())                        
                    self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()                    
                    time.sleep(3)           
                    #WGFM 
                    self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click() 
                    time.sleep(3)
                    handle = self.driver.current_window_handle      
                    self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[5]/div[2]').click()
                    time.sleep(3)
                    handles = self.driver.window_handles
                    for newhandle in handles:
                        # 開啟新的視窗
                        if newhandle!=handle:
                            self.driver.switch_to.window(newhandle)
                            # 2022.12.09新增api status 判斷
                            headers = {'content-type':'application/json; charset=utf-8'}
                            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                            token = r.json()['token']
                            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                            print (r.status_code)
                            self.assertEqual(r.status_code, 200)
                            #
                            time.sleep(30)
                            tilt =self.driver.title
                            print(tilt)
                            self.images.append(self.driver.get_screenshot_as_base64())
                            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")              
                            self.driver.switch_to.default_content()                    
                            self.driver.quit()

    def test_moWGFM(self):
        """手機WGFM測試"""
        self.chrome_options = Options()
#        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.delete_all_cookies()
        self.driver.get('https://stg-t1.rpgp.cc/')
        element=WebDriverWait(self.driver,120,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
        )
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        #優惠彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header[1]/div/div[1]/div/div[2]/div/div[1]')
        login.click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/div/input").send_keys("qatest1")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[4]/div[1]/input").send_keys("aA19890610")
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.find_element(By.NAME, "登录").click()
        time.sleep(3)        
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[1]').click()  
        time.sleep(3)
        #wgfm
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdWGFM1"]').click()  
        time.sleep(3)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                # 2022.12.09新增api status 判斷
                headers = {'content-type':'application/json; charset=utf-8'}
                r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                token = r.json()['token']
                r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                print (r.status_code)
                self.assertEqual(r.status_code, 200)
                #
                time.sleep(30)                         
                tilt =self.driver.title
                print(tilt)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.assertNotEqual(tilt, "PGG - 专业娱乐平台")              
                self.driver.switch_to.default_content()                    
                self.driver.switch_to.window(handles[0])
                self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/button[5]/span[1]/div').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[1]/div/div[10]/div/div[1]').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="checkbox-list-label-en-US"]/span').click()
                self.driver.find_element(By.XPATH,' //*[@id="root"]/div[2]/div[2]/div').click()                                  
                element=WebDriverWait(self.driver,120,1).until(
                #條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
                )
                    #公告彈窗
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():                       
                    self.images.append(self.driver.get_screenshot_as_base64())
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                        
                    time.sleep(3)
                     #優惠彈窗   
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[3]").is_displayed():
                    self.images.append(self.driver.get_screenshot_as_base64())                        
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                    
                    time.sleep(3)           
                    #WGFM
                    handle = self.driver.current_window_handle   
                    self.driver.find_element(By.XPATH, '//*[@id="gameIdWGFM1"]').click()  
                    time.sleep(3)
                    handles = self.driver.window_handles
                    for newhandle in handles:
                        # 開啟新的視窗
                        if newhandle!=handle:
                            self.driver.switch_to.window(newhandle)
                            # 2022.12.09新增api status 判斷
                            headers = {'content-type':'application/json; charset=utf-8'}
                            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                            token = r.json()['token']
                            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                            print (r.status_code)
                            self.assertEqual(r.status_code, 200)
                            #
                            time.sleep(30)
                            tilt =self.driver.title
                            print(tilt)
                            self.images.append(self.driver.get_screenshot_as_base64())
                            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")              
                            self.driver.switch_to.default_content()                    
                            self.driver.quit()

    def test_pptf(self):
        """pptf虛擬體育"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
#        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
        self.driver.delete_all_cookies()
        self.base_url = "https://stg-t1.rpgp.cc/"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        element=WebDriverWait(self.driver,30,1).until(
#        條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )        
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
#        #優惠彈窗 
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[4]/div[2]/div[1]/span')
        login.click()           
        element=self.driver.find_element(By.ID,'username')
        element.send_keys('qatest1')
        element.send_keys('\ue004')
        element =self.driver.find_element(By.ID,'password')
        element.send_keys('aA19890610')   
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div[5]/div[3]/span').click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)          
        #pptf虛擬體育   
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[4]/div[2]').click()     
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/div[1]').click() 
        time.sleep(3)
        # 2022.12.09新增api status 判斷
        headers = {'content-type':'application/json; charset=utf-8'}
        r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
        token = r.json()['token']
        r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
        print (r.status_code)
        self.assertEqual(r.status_code, 200)
        #
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="2700253"]/div/iframe'))
        time.sleep(40)
        tilt =self.driver.find_element(By.XPATH,"/html/head/title").get_attribute('textContent')
        print(tilt)
        self.assertNotEqual(tilt, "PGG - 专业娱乐平台")
        self.images.append(self.driver.get_screenshot_as_base64())        
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[3]/div/div').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="simple-menu"]/div[3]/ul/li[1]').click()
        element=WebDriverWait(self.driver,60,1).until(
#        條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )                
            #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
            #優惠彈窗   
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)           
            #pptf虛擬體育 
            self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
            time.sleep(3)
            self.images.append(self.driver.get_screenshot_as_base64())
            pptf =self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[4]/div[2]')
            self.driver.execute_script("arguments[0].scrollIntoView();", pptf)
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[4]/div[2]').click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, ' //*[@id="root"]/div[3]/div/div[1]/div[2]/div[2]').click() 
            time.sleep(5)
            # 2022.12.09新增api status 判斷
            headers = {'content-type':'application/json; charset=utf-8'}
            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
            token = r.json()['token']
            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
            print (r.status_code)
            self.assertEqual(r.status_code, 200)
            #
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="2700251"]/div/iframe'))
            time.sleep(40)
            tilt =self.driver.title
            tilt =self.driver.find_element(By.XPATH,"/html/head/title").get_attribute('textContent')
            print(tilt)
            self.images.append(self.driver.get_screenshot_as_base64())
            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")
            self.driver.close()

    def test_mopptf(self):
        """手機pptf虛擬體育測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.delete_all_cookies()
        self.driver.get('https://stg-t1.rpgp.cc/')
        element=WebDriverWait(self.driver,30,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
        )
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        #優惠彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header[1]/div/div[1]/div/div[2]/div/div[1]')
        login.click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/div/input").send_keys("qatest1")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[4]/div[1]/input").send_keys("aA19890610")
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.find_element(By.NAME, "登录").click()
        time.sleep(3)        
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[1]').click()  
        time.sleep(3)
        self.images.append(self.driver.get_screenshot_as_base64())       
        self.driver.find_element(By.XPATH, '//*[@id="gameType2"]').click()  
        time.sleep(3)
        handle = self.driver.current_window_handle 
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[2]/span/img').click()
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                # 2022.12.09新增api status 判斷
                headers = {'content-type':'application/json; charset=utf-8'}
                r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                token = r.json()['token']
                r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                print (r.status_code)
                self.assertEqual(r.status_code, 200)
                #
                time.sleep(30)                         
                tilt =self.driver.title
                print(tilt)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.assertNotEqual(tilt, "PGG - 专业娱乐平台")
                self.driver.close              
                self.driver.switch_to.default_content()                    
                self.driver.switch_to.window(handles[0])
                self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/header/div[1]').click()
                time.sleep(3)            
                self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/button[5]/span[1]/div').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[1]/div/div[10]/div/div[1]').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@id="checkbox-list-label-en-US"]/span').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH,' //*[@id="root"]/div[2]/div[2]/div').click()                                  
                element=WebDriverWait(self.driver,30,1).until(
                #條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
                )
                #以下彈窗請依照設定進行執行或非執行
                #公告彈窗
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():                       
                    self.images.append(self.driver.get_screenshot_as_base64())
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                        
                    time.sleep(3)
                     #優惠彈窗   
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[3]").is_displayed():
                    self.images.append(self.driver.get_screenshot_as_base64())                        
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                    
                    time.sleep(3)           
                    #pptf
                    self.driver.find_element(By.XPATH, '//*[@id="gameType2"]').click()  
                    handle = self.driver.current_window_handle 
                    time.sleep(3)
                    self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[1]/span/img').click()
                    self.images.append(self.driver.get_screenshot_as_base64())  
                    handles = self.driver.window_handles
                    for newhandle in handles:
                        # 開啟新的視窗
                        if newhandle!=handle:
                            self.driver.switch_to.window(newhandle)
                            # 2022.12.09新增api status 判斷
                            headers = {'content-type':'application/json; charset=utf-8'}
                            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                            token = r.json()['token']
                            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                            print (r.status_code)
                            self.assertEqual(r.status_code, 200)
                            #
                            time.sleep(30)
                            tilt =self.driver.title
                            print(tilt)
                            self.images.append(self.driver.get_screenshot_as_base64())
                            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")              
                            self.driver.switch_to.default_content()                    
                            self.driver.quit()
                            
    def test_BTI(self):
        """BTI測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
#        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
        self.driver.delete_all_cookies()
        self.base_url = "https://stg-t1.rpgp.cc/"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        element=WebDriverWait(self.driver,30,1).until(
#        條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )        
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
#        #優惠彈窗 
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[4]/div[2]/div[1]/span')
        login.click()           
        element=self.driver.find_element(By.ID,'username')
        element.send_keys('qatest1')
        element.send_keys('\ue004')
        element =self.driver.find_element(By.ID,'password')
        element.send_keys('aA19890610')   
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[5]/div[3]/span").click()
        time.sleep(3)          
        #BTI體育  
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        BTI =self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[3]/div[2]')
        self.driver.execute_script("arguments[0].scrollIntoView();", BTI)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[3]/div[2]').click()     
        time.sleep(3)
        # 2022.12.09新增api status 判斷
        headers = {'content-type':'application/json; charset=utf-8'}
        r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
        token = r.json()['token']
        r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
        print (r.status_code)
        self.assertEqual(r.status_code, 200)
        #
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div/iframe'))
        time.sleep(40)
        tilt =self.driver.find_element(By.XPATH,"/html/head/title").get_attribute('textContent')
        print(tilt)
        self.images.append(self.driver.get_screenshot_as_base64())
        self.assertNotEqual(tilt, "PGG - 专业娱乐平台")        
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[3]/div/div').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="simple-menu"]/div[3]/ul/li[1]').click()
        self.images.append(self.driver.get_screenshot_as_base64())
        element=WebDriverWait(self.driver,60,1).until(
#        條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[3]/div/div'))
        )               
            #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            time.sleep(3)
            #優惠彈窗   
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(3)           
            ##BTI體育
            self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[3]/div[1]').click()     
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
            BTI =self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[3]/div[2]')
            self.driver.execute_script("arguments[0].scrollIntoView();", BTI)
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[3]/div[2]').click()  
            time.sleep(2)
            # 2022.12.09新增api status 判斷
            headers = {'content-type':'application/json; charset=utf-8'}
            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
            token = r.json()['token']
            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
            print (r.status_code)
            self.assertEqual(r.status_code, 200)
            #
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div/iframe'))
            time.sleep(40)
            tilt =self.driver.title
            tilt =self.driver.find_element(By.XPATH,"/html/head/title").get_attribute('textContent')
            print(tilt)
            self.images.append(self.driver.get_screenshot_as_base64())
            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")
            self.driver.close()                                                                                                                 

    def test_moBTI(self):
        """手機BTI測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.delete_all_cookies()
        self.driver.get('https://stg-t1.rpgp.cc/')
        element=WebDriverWait(self.driver,60,1).until(
        #條件：直到元素載入完成
        EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
        )
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        #優惠彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():
            self.images.append(self.driver.get_screenshot_as_base64())
            self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()
        time.sleep(2)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header[1]/div/div[1]/div/div[2]/div/div[1]')
        login.click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/div/input").send_keys("qatest1")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[4]/div[1]/input").send_keys("aA19890610")
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.find_element(By.NAME, "登录").click()
        time.sleep(3)        
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[1]').click()  
        time.sleep(2)
        #MOBTI
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdBTI1"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                headers = {'content-type':'application/json; charset=utf-8'}
                r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                token = r.json()['token']
                r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                print (r.status_code)
                self.assertEqual(r.status_code, 200)
                #
                time.sleep(30)                         
                tilt =self.driver.title
                print(tilt)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.assertNotEqual(tilt, "PGG - 专业娱乐平台")              
                self.driver.switch_to.default_content()                    
                self.driver.switch_to.window(handles[0])
                self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/button[5]/span[1]/div').click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[1]/div/div[10]/div/div[1]').click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, '//*[@id="checkbox-list-label-en-US"]/span').click()
                self.driver.find_element(By.XPATH,' //*[@id="root"]/div[2]/div[2]/div').click()                                  
                element=WebDriverWait(self.driver,60,1).until(
                #條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div'))
                )
                    #公告彈窗
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div").is_displayed():                       
                    self.images.append(self.driver.get_screenshot_as_base64())
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                        
                    time.sleep(2)
                     #優惠彈窗   
                if  self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[3]").is_displayed():
                    self.images.append(self.driver.get_screenshot_as_base64())                        
                    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[4]").click()                    
                    time.sleep(2)           
                    #MOBTI
                    handle = self.driver.current_window_handle   
                    self.driver.find_element(By.XPATH, '//*[@id="gameIdBTI1"]').click()  
                    time.sleep(2)
                    handles = self.driver.window_handles
                    for newhandle in handles:
                        # 開啟新的視窗
                        if newhandle!=handle:
                            self.driver.switch_to.window(newhandle)
                            headers = {'content-type':'application/json; charset=utf-8'}
                            r = requests.post('https://stg-t1.rpgp.cc/api/Player/Login',headers=headers,data = json.dumps({"username":"qatest1","password":"aA19890610","platformtype":0}))
                            token = r.json()['token']
                            r= requests.post('https://stg-t1.rpgp.cc/api/Game/lobby/geturl',headers={"Authorization": "Bearer {}".format(token),"token" : token}, timeout=40)
                            print (r.status_code)
                            self.assertEqual(r.status_code, 200)
                            #
                            time.sleep(30)
                            tilt =self.driver.title
                            print(tilt)
                            self.images.append(self.driver.get_screenshot_as_base64())
                            self.assertNotEqual(tilt, "PGG - 专业娱乐平台")              
                            self.driver.switch_to.default_content()                    
                            self.driver.quit()
                            
if __name__ == '__main__':
    
#       以下部分為測試項目，若上面Class的Def Test有需要測試時必須加入
#       範本為: Test('測試項目名稱'),
    Case1 = unittest.TestSuite()
    Case1.addTests([ 
          Test2('test_SABA'),
          Test2('test_mosaba'),
          Test2('test_Betconstruct'),
          Test2('test_moBetconstruct'),
          Test2('test_sbobet'),
          Test2('test_mosbobet'),
          Test2('test_wgvia'),
          Test2('test_mowgvia'),
          Test2('test_AWC_COCKFIGH'),
          Test2('test_moAWC_COCKFIGH'),
          Test2('test_AWC_RCB'),
          Test2('test_moAWC_RCB'),
          Test2('test_WGFM'),
          Test2('test_moWGFM'),
          Test2('test_pptf'),
          Test2('test_mopptf'),
          Test2('test_BTI'),
          Test2('test_moBTI'),
    ]) 
              
    with(open('./result.html', 'wb')) as fp:
#       以下為測試報告內容撰寫部分
#       title為頁面報告名稱
#       description為描述
#       tester為測試者
#       language為測試報告使用的語系，目前僅支援zh-CN與en語系        
        runner = HTMLTestRunner(
            stream=fp,
            title='Selenium前台測試報告',
            description='Release1.36',
            tester='Sinyi.wang',
            language='zh-CN',
        )
        runner.run(
#       testlist: 想要跑什麼測試。
#       rerun: 重跑次數。
#       save_last_run: 是否保存最後一個測試結果。
            #testlist=Fulltest,
            testlist=Case1,
            rerun=0,
            save_last_run=True
        )           