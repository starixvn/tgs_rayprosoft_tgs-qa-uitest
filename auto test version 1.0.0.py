#auto test version 1.0.0
import unittest
import time
import random
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

class Test(unittest.TestCase):
    """前站自動化測試"""
    
    #測試前注意測試項目及帳號條件已免出錯
    def test_mobileregister(self):
        """註冊測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://dev-t1.rpgp.cc/')
        self.vars = {}
        time.sleep(1)
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
#        self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#        time.sleep(1)
#        #優惠彈窗
#        self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#        time.sleep(2)
        #正確註冊
        self.driver.find_element(By.CSS_SELECTOR, ".dfHtWM").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").click()
        ###每次測試都必須更改
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").send_keys("0614stgtest8")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(4) .sc-dfRKBO").send_keys("TgsP@ssw0rd")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(5) .sc-dfRKBO").send_keys("TgsP@ssw0rd")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-gGsJSs").click()
        time.sleep(1)
        print("正確註冊 Test pass")   
        
    def test_mobilere_register(self):
        """重複註冊測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        self.vars = {}
        time.sleep(1)
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
#        self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#        time.sleep(1)
#        #優惠彈窗
#        self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#        time.sleep(2)
        #重複註冊
        self.driver.find_element(By.CSS_SELECTOR, ".dfHtWM").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").click()
        ###每次測試都必須更改
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").send_keys("0614stgtest8")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(4) .sc-dfRKBO").send_keys("TgsP@ssw0rd")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(5) .sc-dfRKBO").send_keys("TgsP@ssw0rd")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-gGsJSs").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".sc-exYRda").click()
        print("重複註冊 Test pass")              
                           
    def test_mobileerrregister(self):
        """註冊帳號錯誤測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        self.vars = {}
        time.sleep(1)
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
#        self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#        time.sleep(1)
#        #優惠彈窗
#        self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#        time.sleep(2)
        #帳號註冊小於6碼
        self.driver.find_element(By.CSS_SELECTOR, ".dfHtWM").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").click()
        ###每次測試都必須更改
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").send_keys("stgte")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(4) .sc-dfRKBO").send_keys("TgsP@ssw0rd")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(5) .sc-dfRKBO").send_keys("TgsP@ssw0rd")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-gGsJSs").click()
        time.sleep(2)
        if (self.driver.find_element(By.CSS_SELECTOR,".sc-jBQhSp")):
            self.driver.find_element(By.CSS_SELECTOR, ".sc-exYRda").click()
            print("帳號註冊小於6碼 Test pass")
            
    def test_mobilelogin(self):
        """正確登入測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        self.vars = {}
        time.sleep(1)
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
#       self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#       time.sleep(1)
#       #優惠彈窗
#       self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#       time.sleep(2)   
        self.driver.find_element(By.CSS_SELECTOR, ".kUAJgD").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").click()
        #帳號密碼測試要更換
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").send_keys("qatest1")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(4) .sc-dfRKBO").send_keys("aA19890610")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-gGsJSs:nth-child(1)").click()
        time.sleep(1)
        self.images.append(self.driver.get_screenshot_as_base64())
        while (self.driver.find_element(By.CSS_SELECTOR,'.sc-mWPeY').is_displayed):
            self.assertTrue (self.driver.find_element(By.XPATH,"//*[text()='qatest1']"))
            print('正確登入')
            break
        self.driver.quit()
        
    def test_mobile_account_err_login(self):
        """帳號小於6碼錯誤測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        self.vars = {}
        time.sleep(1)
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
#       self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#       time.sleep(1)
#       #優惠彈窗
#       self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#       time.sleep(2)   
        self.driver.find_element(By.CSS_SELECTOR, ".kUAJgD").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").click()
        #帳號密碼測試要更換
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").send_keys("qate")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(4) .sc-dfRKBO").send_keys("aA19890610")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-gGsJSs:nth-child(1)").click()
        time.sleep(1)
        if(self.driver.find_element(By.CSS_SELECTOR,'.sc-jBQhSp').is_displayed):
            a=self.driver.find_element(By.CSS_SELECTOR,'.sc-jBQhSp').get_attribute('innerHTML')
            b='帐号或密码错误'
            self.assertEqual(a,b,'帳號小於6碼錯誤test fail,請確認截圖畫面')
            print('帳號小於6碼錯誤test pass')
        self.driver.quit()  
    
    def test_mobile_password_err_login(self):
        """密碼小於6碼錯誤測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        self.vars = {}
        time.sleep(1)
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
#       self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#       time.sleep(1)
#       #優惠彈窗
#       self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#       time.sleep(2)   
        self.driver.find_element(By.CSS_SELECTOR, ".kUAJgD").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").click()
        #帳號密碼測試要更換
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").send_keys("qatest1")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(4) .sc-dfRKBO").send_keys("aA198")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-gGsJSs:nth-child(1)").click()
        time.sleep(1)
        self.images.append(self.driver.get_screenshot_as_base64())
        if(self.driver.find_element(By.CSS_SELECTOR,'.sc-jBQhSp').is_displayed):
            a=self.driver.find_element(By.CSS_SELECTOR,'.sc-jBQhSp').get_attribute('innerHTML')
            b='帐号或密码错误' 
            self.assertEqual(a,b,'密碼小於6碼錯誤test fail,請確認截圖畫面')
            print('密碼小於6碼錯誤test pass')
        self.driver.quit()          

    def test_mobile_special_account_err_login(self):
        """帳號特殊符號測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        self.vars = {}
        time.sleep(1)
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
#       self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#       time.sleep(1)
#       #優惠彈窗
#       self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#       time.sleep(2)   
        self.driver.find_element(By.CSS_SELECTOR, ".kUAJgD").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").click()
        #帳號密碼測試要更換
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").send_keys("qate#####")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(4) .sc-dfRKBO").send_keys("aA19890610")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-gGsJSs:nth-child(1)").click()
        time.sleep(1)
        self.images.append(self.driver.get_screenshot_as_base64())
        if(self.driver.find_element(By.CSS_SELECTOR,'.sc-jBQhSp').is_displayed):
            a=self.driver.find_element(By.CSS_SELECTOR,'.sc-jBQhSp').get_attribute('innerHTML')
            b='帐号或密码错误' 
            self.assertEqual(a,b,'帳號特殊符號test fail,請確認截圖畫面')
            print('帳號特殊符號test pass')
        self.driver.quit()        

    def test_mobile_blank_account_err_login(self):
        """帳號空白測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        self.vars = {}
        time.sleep(1)
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
#       self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#       time.sleep(1)
#       #優惠彈窗
#       self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#       time.sleep(2)   
        self.driver.find_element(By.CSS_SELECTOR, ".kUAJgD").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").click()
        #帳號密碼測試要更換
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(4) .sc-dfRKBO").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-gGsJSs:nth-child(1)").click()
        time.sleep(1)
        self.images.append(self.driver.get_screenshot_as_base64())
        if(self.driver.find_element(By.CSS_SELECTOR,'.sc-jBQhSp').is_displayed):
            a=self.driver.find_element(By.CSS_SELECTOR,'.sc-jBQhSp').get_attribute('innerHTML')
            b='帐号或密码错误' 
            self.assertEqual(a,b,'帳號空白test fail,請確認截圖畫面')
            print('帳號空白test pass')
        self.driver.quit()        

    def test_mobile_overlength_account_err_login(self):
        """帳號超過限制長度測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        self.vars = {}
        time.sleep(1)
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
#       self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#       time.sleep(1)
#       #優惠彈窗
#       self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#       time.sleep(2)   
        self.driver.find_element(By.CSS_SELECTOR, ".kUAJgD").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").click()
        #帳號密碼測試要更換
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").send_keys("testtesttesttesttest")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(4) .sc-dfRKBO").send_keys("aA19890610")
        self.driver.find_element(By.CSS_SELECTOR, ".sc-gGsJSs:nth-child(1)").click()
        time.sleep(1)
        self.images.append(self.driver.get_screenshot_as_base64())
        if(self.driver.find_element(By.CSS_SELECTOR,'.sc-jBQhSp').is_displayed):
            a=self.driver.find_element(By.CSS_SELECTOR,'.sc-jBQhSp').get_attribute('innerHTML')
            b='帐号或密码错误' 
            self.assertEqual(a,b,'帳號超過限制長度test fail,請確認截圖畫面')
            print('帳號超過限制長度test pass')
        self.driver.quit()

    def test_mobile_notentered_account_err_login(self):
        """未輸入帳號密碼顯示測試"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('----incognito')
        mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stg-t1.rpgp.cc/')
        self.vars = {}
        time.sleep(1)
        #以下彈窗請依照設定進行執行或非執行
        #公告彈窗
#       self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#       time.sleep(1)
#       #優惠彈窗
#       self.driver.find_element(By.CSS_SELECTOR, ".sc-huKLiJ").click()
#       time.sleep(2)   
        self.driver.find_element(By.CSS_SELECTOR, ".kUAJgD").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sc-iqtXtF:nth-child(3) .sc-dfRKBO").click()
        self.images.append(self.driver.get_screenshot_as_base64())
        username = self.driver.find_element(By.CSS_SELECTOR,'.sc-dfRKBO').get_attribute("placeholder")
        password = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[1]/div[4]/div[1]/input').get_attribute("placeholder")
        Comparisonusername ='用户名'
#        Comparisonpassword ='密码'
        Comparisonpassword ='密'
        self.assertEqual(username,Comparisonusername,'未輸入帳號密碼顯示Test Fail,請確認截圖畫面')
        self.assertEqual(password,Comparisonpassword,'未輸入帳號密碼顯示Test Fail,請確認截圖畫面')
        print('未輸入帳號密碼顯示test pass')
        self.driver.quit()                
        
if __name__ == '__main__':
        
    mobile = unittest.TestSuite()
    mobile.addTests([
        #Test('test_mobileerrregister'),
        Test('test_mobile_notentered_account_err_login'),

     ])   

    with(open('./result.html', 'wb')) as fp:
#       以下為測試報告內容撰寫部分
#       title為頁面報告名稱
#       description為描述
#       tester為測試者
#       language為測試報告使用的語系，目前僅支援zh-CN與en語系        
        runner = HTMLTestRunner(
            stream=fp,
            title='Selenium真人遊戲測試報告',
            description='',
            tester='蜥蜴',
            language='zh-CN',
        )
        runner.run(
#       testlist: 想要跑什麼測試。
#       rerun: 重跑次數。
#       save_last_run: 是否保存最後一個測試結果。
            testlist=mobile,
            rerun=0,
            save_last_run=False
        )           