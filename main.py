from selenium import webdriver
import time
import os

chrome_driver_path = 'C:\\Users\\hrath\\Downloads\\chromedriver_win32\\chromedriver.exe'
TWITTER_ID = '@interne87478960'
TWITTER_P_WORD = os.environ['PASSWORD']


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(50)
        self.down = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.up = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)

    def tweet_at_provider(self, id, pass_w):
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(8)
        t_id = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        t_id.send_keys(id)
        time.sleep(1)
        next_btn = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
        next_btn.click()
        time.sleep(6)
        pass_input = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div/input')
        pass_input.send_keys(pass_w)
        time.sleep(1)
        log_in_btn = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        log_in_btn.click()
        time.sleep(6)


internet_complainer = InternetSpeedTwitterBot(chrome_driver_path)
internet_complainer.get_internet_speed()
internet_complainer.tweet_at_provider(TWITTER_ID, TWITTER_P_WORD)
print(f'upload {internet_complainer.up}')
print(f'download {internet_complainer.down}')