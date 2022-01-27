from selenium import webdriver
class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\hrath\\Downloads\\chromedriver_win32\\chromedriver.exe')
        self.up = 0
        self.down = 0
    def get_internet_speed(self):

    def tweet_at_provider(self):



internet_complainer = InternetSpeedTwitterBot()
internet_complainer.get_internet_speed()
internet_complainer.tweet_at_provider()