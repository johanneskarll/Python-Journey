TWTUSERNAME = ""
TWTPASS = ""
twitteraddr = "https://www.twitter.com"
speedtestaddr = "https://www.speedtest.net/"
PROM_DOWN = 150
PROM_UP = 100

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot:
    def __init__ (self):
        self.up = 0
        self.down = 0
        self.chromeopt = Options()
        self.chromeopt.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1080,1000)
        self.driver.get(speedtestaddr)

    
    def get_internet_speed(self):
        self.gobutton = self.driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.gobutton.click()
        time.sleep(50)

        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
    
    def tweet_at_provider(self,realup,realdown):
        # Switch to the new window
        self.driver.switch_to.new_window('tab')
        self.driver.get(twitteraddr)
        time.sleep(3)
        self.signupbutton = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        self.signupbutton.click()
        time.sleep(5)
        self.xusernamebutton = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.xusernamebutton.send_keys(TWTUSERNAME)

        self.nextbutton = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        self.nextbutton.click()

        time.sleep(4)
        self.xpasswordbutton = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.xpasswordbutton.send_keys(TWTPASS)
        self.xpasswordbutton.send_keys(Keys.ENTER)

        time.sleep(3)
        self.inputtext = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div') 
        self.inputtext.send_keys(f"Hey internet provider,why is my internet speed {realdown}down/{realup}up when I pay for {PROM_DOWN}down/{PROM_UP}up?") 

        time.sleep(2)
        self.postbutton = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        self.postbutton.click()
        
 
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider(bot.down.text,bot.up.text)
