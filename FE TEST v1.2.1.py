# version 1.2.1
# version modification 1.1 真人、棋牌遊戲完成，新增iframe測試
# version modification 1.2體育完成
# version modification 1.2.1撰寫電競
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from multiprocessing.connection import wait
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from XTestRunner import HTMLTestRunner
from XTestRunner import XMLTestRunner
from XTestRunner import SMTP

class Test(unittest.TestCase):
    """前站真人測試"""
    def test_login(self):
        """登入測試"""
        # 啟用Chrome參數  
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
        self.base_url = "https://stg-t1.rpgp.cc/"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(7)
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
        if  self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[4]/div[2]/div[1]/span')
        login.click()           
        element=self.driver.find_element(By.ID,'username')
        element.send_keys('qatest1')
        element.send_keys('\ue004')
        element =self.driver.find_element(By.ID,'password')
        element.send_keys('aA19890610')   
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[5]/div[3]/span").click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.close()
        
    def test_mobilelogin(self):
        """手機登入測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        self.vars = {}
        time.sleep(3)
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
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.close()
            
    def test_moallbet(self):
        """手機歐博測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        self.vars = {}
        time.sleep(3)
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
        handle = self.driver.current_window_handle
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[1]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.find_element(By.XPATH, '//*[@id="gameType6"]').click()    
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.ID,"presetVideo"))
                )
                time.sleep(2)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.close()
        self.driver.switch_to.window(handles[0])   
        self.driver.close()
            
    def test_allbet(self):
        """歐博測試"""
         # 啟用Chrome參數  
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
        login = self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[4]/div[2]/div[1]/span')
        login.click()           
        element=self.driver.find_element(By.ID,'username')
        element.send_keys('qatest1')
        element.send_keys('\ue004')
        element =self.driver.find_element(By.ID,'password')
        element.send_keys('aA19890610')   
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[5]/div[3]/span").click()
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(5)
        #歐博真人
        handle = self.driver.current_window_handle
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[1]/span').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div/div/div[1]/div[2]').click()
        self.images.append(self.driver.get_screenshot_as_base64())
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.CLASS_NAME,"bg"))
                )
                time.sleep(2)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.close()
        self.driver.switch_to.window(handles[0])   
        self.driver.close()        
    
    def test_mowm(self):
        """手機wm測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        self.vars = {}
        time.sleep(3)
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
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[1]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle
        self.driver.find_element(By.XPATH,'//*[@id="gameIdWMTF6"]').click()
        self.images.append(self.driver.get_screenshot_as_base64())    
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
           if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
#                element=WebDriverWait(self.driver,30,1).until(
                # 條件：直到元素載入完成
#                EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[29]/div[3]/div[7]'))
#               )
                time.sleep(8)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.close()
                
        self.driver.switch_to.window(handles[0])   
        self.driver.close()        
        
    def test_wm(self):
        """wm測試"""
        # 啟用Chrome參數  
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        #wm真人
        handle = self.driver.current_window_handle 
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[1]/div[1]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div/div/div[5]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        handles = self.driver.window_handles
        for newhandle in handles:
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
#                element=WebDriverWait(self.driver,30,0.5).until
#                (
                # 條件：直到元素載入完成                
#                EC.presence_of_element_located((By.ID,'extend-container'))
#                )
                time.sleep(12)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.close() 
        self.driver.switch_to.window(handles[0]) 
        self.driver.close()
        
    def test_mosw(self):
        """手機sw測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        time.sleep(3)
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
        handle = self.driver.current_window_handle
        self.driver.find_element(By.XPATH, '//*[@id="gameIdSWTF6"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,"/html/body/sw-root/ng-component/div/ng-component/div/div[3]/sw-footer/div/div[1]/div/div[1]"))
                )
                self.images.append(self.driver.get_screenshot_as_base64()) 
                time.sleep(2)
                self.driver.close()
        self.driver.switch_to.window(handles[0])   
        self.driver.close()       
            
    def test_sw(self):
        """sw測試""" 
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        #sw真人     
        handle = self.driver.current_window_handle 
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[1]/div[1]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div/div/div[8]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        handles = self.driver.window_handles
        for newhandle in handles:
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.CLASS_NAME,"header__logo"))
                )
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.close()         
        self.driver.switch_to.window(handles[0]) 
        self.driver.close()
   
    def test_modg(self):
        """手機dg測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        time.sleep(3)
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
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[1]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdDG6"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/canvas"))
                )
                time.sleep(5)
                self.images.append(self.driver.get_screenshot_as_base64()) 
                self.driver.close()
        self.driver.switch_to.window(handles[0])   
        self.driver.close()       

    def test_dg(self):
        """dg測試"""
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        #dg真人
        handle = self.driver.current_window_handle    
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[1]/div[1]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div/div/div[3]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        handles = self.driver.window_handles
        for newhandle in handles:
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'//*[@id="layaCanvas"]'))
                )
                time.sleep(7)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.close()         
        self.driver.switch_to.window(handles[0]) 
        self.driver.close()

    def test_moawcsg(self):
        """手機sexy測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        time.sleep(3)
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
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[1]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdAWC_SG6"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'//*[@id="very-specific-design"]'))
                )
                time.sleep(3)
                self.images.append(self.driver.get_screenshot_as_base64()) 
                self.driver.close()
        self.driver.switch_to.window(handles[0])   
        self.driver.close()       
        
    def test_awcsg(self):
        """awc-sg測試"""
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        #awc-sg真人
        handle = self.driver.current_window_handle    
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[1]/div[1]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div/div/div[6]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        handles = self.driver.window_handles
        for newhandle in handles:
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'//*[@id="playerInfo"]'))
                )
                time.sleep(3)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.close()         
        self.driver.switch_to.window(handles[0]) 
        self.driver.close()

    def test_moevotf(self):
        """手機evo測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        time.sleep(3)
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
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[1]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdEVOTF6"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'//*[@id="category-navigator-top_games"]/div'))
                )
                time.sleep(3)
                self.images.append(self.driver.get_screenshot_as_base64()) 
                self.driver.close()
        self.driver.switch_to.window(handles[0])   
        self.driver.close()       
                
    def test_evotf(self):
        """evo測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        #evotf真人
        handle = self.driver.current_window_handle    
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[1]/div[1]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div/div/div[9]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        handles = self.driver.window_handles
        for newhandle in handles:
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'//*[@id="lobby-root"]/div/footer'))
                )
                time.sleep(3)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.close()         
        self.driver.switch_to.window(handles[0]) 
        self.driver.close()

    def test_mopptf(self):
        """手機pptf測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        time.sleep(3)
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
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[1]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdPPTF6"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'//*[@id="balance_header"]'))
                )
                time.sleep(3)
                self.images.append(self.driver.get_screenshot_as_base64()) 
                self.driver.close()
        self.driver.switch_to.window(handles[0])   
        self.driver.close()       
                
    def test_pptf(self):
        """pptf測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        #pptf真人
        handle = self.driver.current_window_handle    
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[1]/div[1]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div/div/div[10]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        handles = self.driver.window_handles
        for newhandle in handles:
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,60,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'//*[@id="game-container"]/div[2]/app-lobby-desktop/div[2]/div[2]/div[1]'))
                )
                time.sleep(3)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.close()         
        self.driver.switch_to.window(handles[0]) 
        self.driver.close()

class Test1(unittest.TestCase):
    """前站棋牌測試"""
    def test_365(self):
        """365測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        #365棋牌
        handle = self.driver.current_window_handle    
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[2]/div[1]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div/div/div[1]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        handles = self.driver.window_handles
        for newhandle in handles:
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'//*[@id="game"]'))
                )
                time.sleep(35)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.close()         
        self.driver.switch_to.window(handles[0]) 
        self.driver.close()     

    def test_mo365(self):
        """手機365測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        time.sleep(3)
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
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[4]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameType8"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'//*[@id="game"]'))
                )
                time.sleep(35)
                self.images.append(self.driver.get_screenshot_as_base64()) 
                self.driver.close()
        self.driver.switch_to.window(handles[0])   
        self.driver.close()                 

    def test_KY(self):
        """KY測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        #365棋牌
        handle = self.driver.current_window_handle    
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[2]/div[1]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div/div/div[2]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        handles = self.driver.window_handles
        for newhandle in handles:
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'/html/body/div[2]'))
                )
                time.sleep(45)
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.close()         
        self.driver.switch_to.window(handles[0]) 
        self.driver.close()     

    def test_moKY(self):
        """手機KY測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        time.sleep(3)
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
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[4]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdKY8"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/canvas'))
                )
                time.sleep(35)
                self.images.append(self.driver.get_screenshot_as_base64()) 
                self.driver.close()
        self.driver.switch_to.window(handles[0])   
        self.driver.close()

class Test2(unittest.TestCase):
    """前站體育測試"""
    def test_SABA(self):
        """SABA測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[1]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/iframe'))
        time.sleep(10)
        self.driver.switch_to.frame("sportsFrame")
        element=WebDriverWait(self.driver,30,0.5).until(
        # 條件：直到元素載入完成
        EC.presence_of_element_located(((By.XPATH,'//*[@id="systemTime"]')))
        )   
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.switch_to.default_content()
        time.sleep(5)
        self.driver.close()         

    def test_mosaba(self):
        """手機saba測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        time.sleep(3)
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
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameType1"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'//*[@id="divMain"]/div[4]'))
                )
                time.sleep(3)
                self.images.append(self.driver.get_screenshot_as_base64()) 
                self.driver.close()
        self.driver.switch_to.window(handles[0])   
        self.driver.close()

    def test_Betconstruct(self):
        """Betconstruct測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[2]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/iframe'))
        time.sleep(10)
        self.driver.switch_to.frame("bcsportsbookiframe")
        element=WebDriverWait(self.driver,30,0.5).until(
        # 條件：直到元素載入完成
        EC.presence_of_element_located(((By.XPATH,'//*[@id="main-header-container"]/ng-include/ng-include/div')))
        )   
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.switch_to.default_content()
        time.sleep(5)
        self.driver.close()       

    def test_moBetconstruct(self):
        """手機Betconstruct測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        time.sleep(3)
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
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdBC1"]').click()  
        time.sleep(2)
#        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if handle!=newhandle:
                self.driver.switch_to.window(newhandle)
                self.images.append(self.driver.get_screenshot_as_base64())
                time.sleep(20)
                self.driver.switch_to.window(self.driver.window_handles[1]) 
                print("bc無法給截圖只能看文字")   
                self.driver.close() 
        self.driver.switch_to.window(handles[0])   
        self.driver.close()    

    def test_sbobet(self):
        """sbobet測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
#        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[3]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/iframe'))
        time.sleep(10)
        element=WebDriverWait(self.driver,30,0.5).until(
        # 條件：直到元素載入完成
        EC.presence_of_element_located(((By.XPATH,'//*[@id="blue-bar-inner"]')))
        )   
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.switch_to.default_content()
        time.sleep(5)
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
        time.sleep(3)
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
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdSBO1"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'//*[@id="account-links"]/ul/div'))
                )
                time.sleep(3)
                self.images.append(self.driver.get_screenshot_as_base64()) 
                self.driver.close()
        self.driver.switch_to.window(handles[0])   
        self.driver.close()

    def test_wgvia(self):
        """wgvia測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[4]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        handles = self.driver.window_handles
        for newhandle in handles:
            # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                time.sleep(3)
                self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="mainBody"]/iframe'))
                element=WebDriverWait(self.driver,30,1).until(
                 # 條件：直到元素載入完成
                 EC.presence_of_element_located(((By.XPATH,'/html/body/div/div')))
                )   
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.switch_to.default_content()
                time.sleep(3)
        self.driver.close()
        
    def test_mowgvia(self):
        """手機wgvia測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        time.sleep(3)
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
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdWGVIA1"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                time.sleep(3)
                self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="mainBody"]/iframe'))
                element=WebDriverWait(self.driver,30,1).until(
                 # 條件：直到元素載入完成
                 EC.presence_of_element_located(((By.XPATH,'/html/body/div/div')))
                )   
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.switch_to.default_content()
                time.sleep(3)
        self.driver.close()        

    def test_AWC_COCKFIGH(self):
        """AWC_COCKFIGH測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗 
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[1]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div/iframe'))
        element=WebDriverWait(self.driver,40,1).until(
        # 條件：直到元素載入完成
        EC.presence_of_element_located(((By.XPATH,'//*[@id="scaleable-wrapper"]')))
        )   
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.switch_to.default_content()
        time.sleep(5)
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
        time.sleep(3)
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
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdAWC_COCKFIGHT1"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                time.sleep(3)
                element=WebDriverWait(self.driver,40,1).until(
                 # 條件：直到元素載入完成
                 EC.presence_of_element_located(((By.XPATH,'//*[@id="ancBannerBox"]/div')))
                )   
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.switch_to.default_content()
                time.sleep(3)
        self.driver.close()

    def test_AWC_RCB(self):
        """AWC_RCB測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗 
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[2]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div/iframe'))
        element=WebDriverWait(self.driver,40,1).until(
        # 條件：直到元素載入完成
        EC.presence_of_element_located(((By.XPATH,'//*[@id="top"]/div[1]')))
        )   
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.switch_to.default_content()
        time.sleep(10)
        self.driver.close()

    def test_moAWC_RCB(self):
        """手機AWC_RCB測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        time.sleep(3)
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
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdAWC_RCB1"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                time.sleep(3)
                element=WebDriverWait(self.driver,40,1).until(
                 # 條件：直到元素載入完成
                 EC.presence_of_element_located(((By.XPATH,'/html/body/header/div')))
                )   
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.switch_to.default_content()
                time.sleep(3)
        self.driver.close()

    def test_WGFM(self):
        """WGFM測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
#        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗 
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[3]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        handles = self.driver.window_handles
        for newhandle in handles:
            # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                time.sleep(3)
                element=WebDriverWait(self.driver,120,1).until(
                 # 條件：直到元素載入完成
                 EC.presence_of_element_located(((By.XPATH,'//*[@id="header"]')))
                )   
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.switch_to.default_content()
                time.sleep(3)
        self.driver.close()

    def test_moWGFM(self):
        """手機WGFM測試"""
        self.chrome_options = Options()
#        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        time.sleep(3)
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
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameIdWGFM1"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                time.sleep(3)
                element=WebDriverWait(self.driver,40,1).until(
                 # 條件：直到元素載入完成
                 EC.presence_of_element_located(((By.XPATH,'//*[@id="newlobbyRoot"]/div[3]')))
                )   
                self.images.append(self.driver.get_screenshot_as_base64())
                self.driver.switch_to.default_content()
                time.sleep(3)
        self.driver.close()     

    def test_pptf(self):
        """pptf虛擬體育"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
#        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗 
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/div[4]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/div[1]').click() 
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="2700253"]/div/iframe'))
        time.sleep(2)
        element=WebDriverWait(self.driver,30,0.5).until(
        # 條件：直到元素載入完成
        EC.presence_of_element_located(((By.XPATH,'//*[@id="Heading"]')))
        )   
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.switch_to.default_content()
        time.sleep(5)
        self.driver.close()
        
    def test_mopptf(self):
        """手機pptf虛擬體育測試"""
        self.chrome_options = Options()
#        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        time.sleep(3)
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
        self.images.append(self.driver.get_screenshot_as_base64())       
        self.driver.find_element(By.XPATH, '//*[@id="gameType2"]').click()  
        time.sleep(2)
        handle = self.driver.current_window_handle 
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[2]/span/img').click()
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                time.sleep(3)               
                element=WebDriverWait(self.driver,40,1).until(
                 # 條件：直到元素載入完成
                 EC.presence_of_element_located(((By.XPATH,'//*[@id="Heading"]')))
                )   
                self.images.append(self.driver.get_screenshot_as_base64())
                time.sleep(3)
        self.driver.close()
                  
class Test3(unittest.TestCase):
    """前站電競測試"""
    def test_esports(self):
        """esports測試"""    
        # 啟用Chrome參數
        self.chrome_options = Options()
        # 使用無痕模式
#        self.chrome_options.add_argument('----incognito')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.vars = {}
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
            time.sleep(2)
#        #優惠彈窗   
        if self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div").is_displayed():
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[1]").click()
            self.images.append(self.driver.get_screenshot_as_base64())
            time.sleep(2)
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
        #esports電競   
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/div[2]/ul/li[4]/div[1]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[1]/div[2]').click()     
        self.images.append(self.driver.get_screenshot_as_base64())
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div/iframe'))
        time.sleep(10)
        element=WebDriverWait(self.driver,30,0.5).until(
        # 條件：直到元素載入完成
        EC.presence_of_element_located(((By.XPATH,'//*[@id="esport"]/div/div/div/div[1]/div')))
        )   
        self.images.append(self.driver.get_screenshot_as_base64())
        self.driver.switch_to.default_content()
        time.sleep(5)
        self.driver.close()  

    def test_moesports(self):
        """手機esports測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        time.sleep(3)
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
        self.images.append(self.driver.get_screenshot_as_base64())
        handle = self.driver.current_window_handle        
        self.driver.find_element(By.XPATH, '//*[@id="gameType1"]').click()  
        time.sleep(2)
        self.images.append(self.driver.get_screenshot_as_base64())  
        handles = self.driver.window_handles
        for newhandle in handles:   
        # 開啟新的視窗
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)
                element=WebDriverWait(self.driver,30,0.5).until(
                # 條件：直到元素載入完成
                EC.presence_of_element_located((By.XPATH,'//*[@id="divMain"]/div[4]'))
                )
                time.sleep(3)
                self.images.append(self.driver.get_screenshot_as_base64()) 
                self.driver.close()
        self.driver.switch_to.window(handles[0])   
        self.driver.close()

        
if __name__ == '__main__':
    
#       以下部分為測試項目，若上面Class的Def Test有需要測試時必須加入
#       範本為: Test('測試項目名稱'),       
    Fulltest = unittest.TestSuite()
    Fulltest.addTests([
        Test('test_login'),
        Test('test_mobilelogin'),
        Test('test_moallbet'),
        Test('test_allbet'),
        Test('test_mowm'),
        Test("test_wm"),
        Test('test_mosw'),
        Test("test_sw"),
        Test('test_modg'),
        Test("test_dg"),
        Test('test_moawcsg'),
        Test("test_awcsg"),
        Test('test_moevotf'),
        Test("test_evotf"),
        Test('test_mopptf'),
        Test("test_pptf"),
        Test1('test_365'),
        Test1('test_mo365'),
        Test1('test_KY'),
        Test1('test_moKY')               
    ])
    
    mobile = unittest.TestSuite()
    mobile.addTests([
        Test('test_mobilelogin'),
        Test('test_moallbet'),
        Test('test_mowm'),
        Test('test_mosw'),
        Test('test_modg'),
        Test('test_moawcsg'),
        Test('test_moevotf'),
        Test('test_mopptf'),
    ])
    
    Desktop = unittest.TestSuite()
    Desktop.addTests([
        Test('test_login'),
        Test('test_allbet'),
        Test("test_wm"),
        Test("test_sw"),
        Test("test_dg"),
        Test("test_awcsg"),
        Test("test_evotf"),
        Test("test_pptf"),
    ]) 
    
    Case1 = unittest.TestSuite()
    Case1.addTests([ 
#        Test1('test_365'),
#        Test1('test_mo365'),
#        Test1('test_KY'),
#        Test1('test_moKY')
         Test2('test_mopptf'),
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
            description='',
            tester='Sinyiwang',
            language='zh-CN',
        )
        runner.run(
#       testlist: 想要跑什麼測試。
#       rerun: 重跑次數。
#       save_last_run: 是否保存最後一個測試結果。
            testlist=Case1,
            rerun=0,
            save_last_run=True
        )           
                
                                    